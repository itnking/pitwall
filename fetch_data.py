#!/usr/bin/env python3
"""PITWALL — robot de mise à jour quotidien.

Ce script :
  1. charge la base vérifiée  seed_2026.json
  2. récupère EN DIRECT les données F1 via l'API ouverte Jolpica
     (calendrier + horaires de séances, résultats, classements) ;
  3. fusionne le tout et écrit  data.json , le fichier que lit l'app.

Il n'utilise que la bibliothèque standard (aucun pip), et si une source est
indisponible il conserve les données de la graine : l'app n'est jamais cassée.

Pour étendre l'auto-mise-à-jour aux autres championnats (WEC, ELMS, GTWC, DTM,
WRC), ajoute une fonction  update_<serie>()  sur le même modèle que update_f1().
Les sources confirmées lisibles par machine sont notées plus bas.
"""
import json, sys, urllib.request, datetime

JOLPICA = "https://api.jolpi.ca/ergast/f1/2026"
SEASON = "2026"
UA = {"User-Agent": "PITWALL/1.0 (personal calendar)"}

# ----------------------------------------------------------------------------
def get_json(url, timeout=20):
    """GET JSON, ou None si la source est indisponible (jamais d'exception)."""
    try:
        req = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return json.load(r)
    except Exception as e:
        print(f"  ! source indisponible : {url}\n    ({e})", file=sys.stderr)
        return None

def iso(date, time):
    """'2026-06-26' + '13:30:00Z' -> '2026-06-26T13:30:00Z'."""
    if not date or not time:
        return None
    if not time.endswith("Z"):
        time = time.rstrip("Z") + "Z"
    return f"{date}T{time}"

# ----------------------------------------------------------------------------
# F1 — via Jolpica (successeur ouvert d'Ergast). Le calendrier/les noms FR
# proviennent de la graine ; on n'y superpose que le PÉRISSABLE : dates,
# horaires de séances, vainqueurs, classements.
# ----------------------------------------------------------------------------
SESS_FR = [
    ("FirstPractice", "Essais libres 1", False),
    ("SecondPractice", "Essais libres 2", False),
    ("ThirdPractice", "Essais libres 3", False),
    ("SprintQualifying", "Qualifs Sprint", False),
    ("Sprint", "Sprint", False),
    ("Qualifying", "Qualifications", False),
]

def update_f1(seed):
    print("F1 : récupération via Jolpica…")
    races = get_json(f"{JOLPICA}/races.json?limit=100")
    winners = get_json(f"{JOLPICA}/results/1.json?limit=100")
    dstand = get_json(f"{JOLPICA}/driverstandings.json")
    cstand = get_json(f"{JOLPICA}/constructorstandings.json")

    # index des courses F1 de la graine, par numéro de manche
    f1_events = {int(e["r"][1:]): e for e in seed["events"] if e["s"] == "f1" and e.get("r")}

    # --- calendrier + horaires de séances ---
    if races:
        try:
            for R in races["MRData"]["RaceTable"]["Races"]:
                rnd = int(R["round"])
                e = f1_events.get(rnd)
                if not e:
                    continue
                race_date = R.get("date")
                first = R.get("FirstPractice", {}).get("date")
                e["a"] = first or race_date     # début week-end
                e["b"] = race_date              # jour de course
                sessions = []
                for key, label, _ in SESS_FR:
                    s = R.get(key)
                    if s and s.get("date"):
                        t = iso(s["date"], s.get("time", "00:00:00Z"))
                        if t:
                            sessions.append({"n": label, "t": t})
                t = iso(race_date, R.get("time", "00:00:00Z"))
                if t:
                    sessions.append({"n": "Course", "t": t, "race": True})
                if sessions:
                    e["sessions"] = sessions
            print(f"  ✓ {len(races['MRData']['RaceTable']['Races'])} manches mises à jour")
        except (KeyError, TypeError) as e:
            print(f"  ! structure calendrier inattendue : {e}", file=sys.stderr)

    # --- vainqueurs par manche ---
    if winners:
        try:
            for R in winners["MRData"]["RaceTable"]["Races"]:
                rnd = int(R["round"])
                e = f1_events.get(rnd)
                if e and R.get("Results"):
                    e["w"] = R["Results"][0]["Driver"]["familyName"]
        except (KeyError, TypeError) as e:
            print(f"  ! structure résultats inattendue : {e}", file=sys.stderr)

    # --- classement pilotes ---
    if dstand:
        try:
            lst = dstand["MRData"]["StandingsTable"]["StandingsLists"]
            if lst:
                rows = []
                for s in lst[0]["DriverStandings"][:12]:
                    rows.append({
                        "p": int(s["position"]),
                        "n": s["Driver"]["familyName"],
                        "sub": s["Constructors"][0]["name"] if s.get("Constructors") else "",
                        "pts": int(float(s["points"])),
                    })
                rnd = lst[0].get("round", "?")
                seed["standings"]["f1"]["tables"][0]["rows"] = rows
                seed["standings"]["f1"]["round"] = f"après {rnd} manches · {rnd}/22"
                print(f"  ✓ classement pilotes ({len(rows)} lignes)")
        except (KeyError, TypeError, IndexError) as e:
            print(f"  ! structure classement pilotes inattendue : {e}", file=sys.stderr)

    # --- classement constructeurs ---
    if cstand:
        try:
            lst = cstand["MRData"]["StandingsTable"]["StandingsLists"]
            if lst:
                rows = [{"p": int(s["position"]), "n": s["Constructor"]["name"],
                         "pts": int(float(s["points"]))}
                        for s in lst[0]["ConstructorStandings"]]
                seed["standings"]["f1"]["tables"][1]["rows"] = rows
                print(f"  ✓ classement constructeurs ({len(rows)} lignes)")
        except (KeyError, TypeError, IndexError) as e:
            print(f"  ! structure classement constructeurs inattendue : {e}", file=sys.stderr)

    return seed

# ----------------------------------------------------------------------------
# Autres championnats — sources confirmées lisibles par machine :
#   GTWC : https://www.gt-world-challenge-europe.com/standings (+ /drivers, fiches /driver/<id>/<slug>)
#   ELMS : https://elms.alkamelsystems.com/ (timing Al Kamel, PDF + JSON)
#   DTM  : https://www.dtm.com/en/results  (+ standings)
#   WEC  : https://www.fiawec.com/
#   WRC  : https://www.wrc.com/  (live timing partenaire)
# Tant qu'un update_<serie>() n'est pas branché, ces séries gardent les valeurs
# (vérifiées) de la graine. Pour les pages rendues côté client, prévoir un
# rendu headless (Playwright) dans le workflow.
# ----------------------------------------------------------------------------

def main():
    with open("seed_2026.json", encoding="utf-8") as f:
        data = json.load(f)

    data = update_f1(data)
    # update_wec(data) ; update_gtwc(data) ; ...  (à brancher)

    data["generated"] = datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat()
    data["source"] = "robot"
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=1)

    n = len(data["events"])
    print(f"\ndata.json écrit — {n} courses, généré {data['generated']}")

if __name__ == "__main__":
    main()
