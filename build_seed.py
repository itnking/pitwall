#!/usr/bin/env python3
"""Construit seed_2026.json : la base de données « graine » de PITWALL.

Toutes ces données ont été vérifiées aux sources officielles (juin 2026).
Le robot (fetch_data.py) part de cette graine, puis remplace la F1 par les
données live de l'API Jolpica, et produit data.json — le fichier que lit l'app.
"""
import json, datetime

# ----------------------------------------------------------------------------
# CALENDRIER — 6 championnats
# ----------------------------------------------------------------------------
events = []

def ev(s, n, c, co, fl, a, b, r=None, f=None, w=None, tbc=False, sessions=None):
    d = {"s": s, "n": n, "c": c, "co": co, "fl": fl, "a": a, "b": b}
    if r: d["r"] = r
    if f: d["f"] = f
    if w: d["w"] = w
    if tbc: d["tbc"] = True
    if sessions: d["sessions"] = sessions
    events.append(d)

# --- Formula 1 (22 manches) — remplacé en live par Jolpica ---
f1 = [
 ("R1","GP d'Australie","Albert Park, Melbourne","Australie","🇦🇺","2026-03-06","2026-03-08","Russell"),
 ("R2","GP de Chine","Shanghai","Chine","🇨🇳","2026-03-13","2026-03-15","Antonelli"),
 ("R3","GP du Japon","Suzuka","Japon","🇯🇵","2026-03-27","2026-03-29","Antonelli"),
 ("R4","GP de Miami","Miami Intl Autodrome","États-Unis","🇺🇸","2026-05-01","2026-05-03","Antonelli"),
 ("R5","GP du Canada","Montréal — Gilles-Villeneuve","Canada","🇨🇦","2026-05-22","2026-05-24","Antonelli"),
 ("R6","GP de Monaco","Monte-Carlo","Monaco","🇲🇨","2026-06-05","2026-06-07","Antonelli"),
 ("R7","GP de Barcelone","Barcelona-Catalunya","Espagne","🇪🇸","2026-06-12","2026-06-14","Hamilton"),
 ("R8","GP d'Autriche","Red Bull Ring, Spielberg","Autriche","🇦🇹","2026-06-26","2026-06-28",None),
 ("R9","GP de Grande-Bretagne","Silverstone","Royaume-Uni","🇬🇧","2026-07-03","2026-07-05",None),
 ("R10","GP de Belgique","Spa-Francorchamps","Belgique","🇧🇪","2026-07-17","2026-07-19",None),
 ("R11","GP de Hongrie","Hungaroring","Hongrie","🇭🇺","2026-07-24","2026-07-26",None),
 ("R12","GP des Pays-Bas","Zandvoort","Pays-Bas","🇳🇱","2026-08-21","2026-08-23",None),
 ("R13","GP d'Italie","Monza","Italie","🇮🇹","2026-09-04","2026-09-06",None),
 ("R14","GP d'Espagne","Madring, Madrid","Espagne","🇪🇸","2026-09-11","2026-09-13",None),
 ("R15","GP d'Azerbaïdjan","Bakou","Azerbaïdjan","🇦🇿","2026-09-24","2026-09-26",None),
 ("R16","GP de Singapour","Marina Bay","Singapour","🇸🇬","2026-10-09","2026-10-11",None),
 ("R17","GP des États-Unis","COTA, Austin","États-Unis","🇺🇸","2026-10-23","2026-10-25",None),
 ("R18","GP de Mexico","Mexico City","Mexique","🇲🇽","2026-10-30","2026-11-01",None),
 ("R19","GP de São Paulo","Interlagos","Brésil","🇧🇷","2026-11-06","2026-11-08",None),
 ("R20","GP de Las Vegas","Las Vegas Strip","États-Unis","🇺🇸","2026-11-19","2026-11-21",None),
 ("R21","GP du Qatar","Lusail","Qatar","🇶🇦","2026-11-27","2026-11-29",None),
 ("R22","GP d'Abu Dhabi","Yas Marina","Émirats A.U.","🇦🇪","2026-12-04","2026-12-06",None),
]
austria_sessions = [
 {"n":"Essais libres 1","t":"2026-06-26T11:30:00Z"},
 {"n":"Essais libres 2","t":"2026-06-26T15:00:00Z"},
 {"n":"Essais libres 3","t":"2026-06-27T10:30:00Z"},
 {"n":"Qualifications","t":"2026-06-27T14:00:00Z"},
 {"n":"Course","t":"2026-06-28T13:00:00Z","race":True},
]
for r,n,c,co,fl,a,b,w in f1:
    ev("f1",n,c,co,fl,a,b,r=r,w=w,sessions=austria_sessions if r=="R8" else None)

# --- FIA WEC ---
wec = [
 ("6 Heures d'Imola","Imola","Italie","🇮🇹","6H","2026-04-17","2026-04-19","Ferrari #51",False),
 ("6 Heures de Spa","Spa-Francorchamps","Belgique","🇧🇪","6H","2026-05-07","2026-05-09","BMW #15",False),
 ("24 Heures du Mans","Circuit de la Sarthe","France","🇫🇷","24H","2026-06-13","2026-06-14","Toyota #7",False),
 ("6 Heures de São Paulo","Interlagos","Brésil","🇧🇷","6H","2026-07-10","2026-07-12",None,False),
 ("Lone Star Le Mans","COTA, Austin","États-Unis","🇺🇸","6H","2026-09-04","2026-09-06",None,False),
 ("6 Heures de Fuji","Fuji Speedway","Japon","🇯🇵","6H","2026-09-25","2026-09-27",None,False),
 ("Qatar 1812 km","Lusail","Qatar","🇶🇦","~10H","2026-10-20","2026-10-22",None,True),
 ("8 Heures de Bahreïn","Sakhir","Bahreïn","🇧🇭","8H","2026-11-05","2026-11-07",None,False),
]
for n,c,co,fl,f,a,b,w,tbc in wec: ev("wec",n,c,co,fl,a,b,f=f,w=w,tbc=tbc)

# --- ELMS ---
elms = [
 ("R1","4 Heures de Barcelone","Barcelona-Catalunya","Espagne","🇪🇸","2026-04-10","2026-04-12","Forestier/Panis"),
 ("R2","4 Heures du Castellet","Paul Ricard","France","🇫🇷","2026-05-01","2026-05-03","United Autosports"),
 ("R3","4 Heures d'Imola","Imola","Italie","🇮🇹","2026-07-03","2026-07-05",None),
 ("R4","4 Heures de Spa","Spa-Francorchamps","Belgique","🇧🇪","2026-08-21","2026-08-23",None),
 ("R5","4 Heures de Silverstone","Silverstone","Royaume-Uni","🇬🇧","2026-09-11","2026-09-13",None),
 ("R6","4 Heures de Portimão","Algarve","Portugal","🇵🇹","2026-10-08","2026-10-10",None),
]
for r,n,c,co,fl,a,b,w in elms: ev("elms",n,c,co,fl,a,b,r=r,f="4H",w=w)

# --- GT World Challenge Europe ---
gtwc = [
 ("R1","Circuit Paul Ricard","Le Castellet","France","🇫🇷",None,"2026-04-10","2026-04-12","Thiim/Drudi/Sørensen"),
 ("R2","Brands Hatch","Brands Hatch","Royaume-Uni","🇬🇧",None,"2026-05-02","2026-05-03","Auer/Engel"),
 ("R3","Monza","Monza","Italie","🇮🇹","Endurance","2026-05-28","2026-05-31",None),
 ("R4","24 Heures de Spa","Spa-Francorchamps","Belgique","🇧🇪","Endurance","2026-06-23","2026-06-28",None),
 ("R5","Misano","Misano","Italie","🇮🇹","Sprint","2026-07-17","2026-07-19",None),
 ("R6","Magny-Cours","Magny-Cours","France","🇫🇷","Sprint","2026-07-31","2026-08-02",None),
 ("R7","Nürburgring","Nürburgring","Allemagne","🇩🇪","Endurance","2026-08-28","2026-08-30",None),
 ("R8","Zandvoort","Zandvoort","Pays-Bas","🇳🇱","Sprint","2026-09-18","2026-09-20",None),
 ("R9","Barcelona","Barcelona-Catalunya","Espagne","🇪🇸","Sprint","2026-10-02","2026-10-04",None),
 ("R10","Portimão","Algarve","Portugal","🇵🇹","Endurance","2026-10-16","2026-10-18",None),
]
for r,n,c,co,fl,f,a,b,w in gtwc: ev("gtwc",n,c,co,fl,a,b,r=r,f=f,w=w)

# --- DTM ---
dtm = [
 ("R1","Red Bull Ring","Spielberg","Autriche","🇦🇹","2026-04-24","2026-04-26",None),
 ("R2","Zandvoort","Zandvoort","Pays-Bas","🇳🇱","2026-05-22","2026-05-24","Cairoli"),
 ("R3","Lausitzring","DEKRA Lausitzring","Allemagne","🇩🇪","2026-06-19","2026-06-21","Cairoli"),
 ("R4","Norisring","Norisring","Allemagne","🇩🇪","2026-07-03","2026-07-05",None),
 ("R5","Oschersleben","Motorsport Arena","Allemagne","🇩🇪","2026-07-24","2026-07-26",None),
 ("R6","Nürburgring","Nürburgring","Allemagne","🇩🇪","2026-08-14","2026-08-16",None),
 ("R7","Sachsenring","Sachsenring","Allemagne","🇩🇪","2026-09-11","2026-09-13",None),
 ("R8","Hockenheimring","Hockenheimring","Allemagne","🇩🇪","2026-10-09","2026-10-11",None),
]
for r,n,c,co,fl,a,b,w in dtm: ev("dtm",n,c,co,fl,a,b,r=r,w=w)

# --- WRC (14 manches) ---
wrc = [
 ("R1","Rallye Monte-Carlo","Monte-Carlo","Monaco","🇲🇨","2026-01-22","2026-01-25","Solberg"),
 ("R2","Rally de Suède","Umeå","Suède","🇸🇪","2026-02-12","2026-02-15","Evans"),
 ("R3","Safari Rally Kenya","Naivasha","Kenya","🇰🇪","2026-03-12","2026-03-15","Katsuta"),
 ("R4","Rallye de Croatie","Zagreb","Croatie","🇭🇷","2026-04-09","2026-04-12",None),
 ("R5","Rally Islas Canarias","Las Palmas","Espagne","🇪🇸","2026-04-23","2026-04-26","Ogier"),
 ("R6","Rallye du Portugal","Matosinhos","Portugal","🇵🇹","2026-05-07","2026-05-10",None),
 ("R7","Rally du Japon","Aichi/Gifu","Japon","🇯🇵","2026-05-28","2026-05-31","Evans"),
 ("R8","Acropole — Grèce","Lamia","Grèce","🇬🇷","2026-06-25","2026-06-28",None),
 ("R9","Rally d'Estonie","Tartu","Estonie","🇪🇪","2026-07-16","2026-07-19",None),
 ("R10","Rally de Finlande","Jyväskylä","Finlande","🇫🇮","2026-07-30","2026-08-02",None),
 ("R11","Rally du Paraguay","Encarnación","Paraguay","🇵🇾","2026-08-27","2026-08-30",None),
 ("R12","Rally du Chili","Biobío","Chili","🇨🇱","2026-09-10","2026-09-13",None),
 ("R13","Rally d'Italie","Sardaigne","Italie","🇮🇹","2026-10-01","2026-10-04",None),
 ("R14","Rally d'Arabie Saoudite","Jeddah","Arabie S.","🇸🇦","2026-11-11","2026-11-14",None),
]
for r,n,c,co,fl,a,b,w in wrc: ev("wrc",n,c,co,fl,a,b,r=r,w=w)

# ----------------------------------------------------------------------------
# CLASSEMENTS (vérifiés)
# ----------------------------------------------------------------------------
standings = {
 "f1": {"round":"après Barcelone · 7/22","last":{"r":"GP de Barcelone","w":"Lewis Hamilton (Ferrari)"},
   "tables":[
     {"title":"Pilotes","rows":[
       {"p":1,"n":"Antonelli","sub":"Mercedes","pts":156,"c":"#00D7B6"},{"p":2,"n":"Hamilton","sub":"Ferrari","pts":115,"c":"#E8002D"},
       {"p":3,"n":"Russell","sub":"Mercedes","pts":106,"c":"#00D7B6"},{"p":4,"n":"Leclerc","sub":"Ferrari","pts":75,"c":"#E8002D"},
       {"p":5,"n":"Norris","sub":"McLaren","pts":73,"c":"#FF8000"},{"p":6,"n":"Piastri","sub":"McLaren","pts":68,"c":"#FF8000"},
       {"p":7,"n":"Verstappen","sub":"Red Bull","pts":55,"c":"#3671C6"},{"p":8,"n":"Gasly","sub":"Alpine","pts":41,"c":"#00A1E8"},
       {"p":9,"n":"Hadjar","sub":"Red Bull","pts":34,"c":"#3671C6"},{"p":10,"n":"Lawson","sub":"Racing Bulls","pts":None,"c":"#6692FF"}]},
     {"title":"Constructeurs","rows":[
       {"p":1,"n":"Mercedes","pts":262,"c":"#00D7B6"},{"p":2,"n":"Ferrari","pts":190,"c":"#E8002D"},{"p":3,"n":"McLaren","pts":141,"c":"#FF8000"},
       {"p":4,"n":"Red Bull Racing","pts":89,"c":"#3671C6"},{"p":5,"n":"Alpine","pts":60,"c":"#00A1E8"},{"p":6,"n":"Racing Bulls","pts":38,"c":"#6692FF"},
       {"p":7,"n":"Haas","pts":None,"c":"#9CA3AF"},{"p":8,"n":"Williams","pts":None,"c":"#37BEDD"},{"p":9,"n":"Audi","pts":None,"c":"#B0B4B8"},
       {"p":10,"n":"Aston Martin","pts":None,"c":"#229971"},{"p":11,"n":"Cadillac","pts":None,"c":"#C7A14E"}]}]},
 "wec": {"round":"après Le Mans · 3/8","last":{"r":"24 Heures du Mans","w":"Toyota #7 — Kobayashi / Conway / de Vries"},
   "note":"Constructeurs Hypercar : Toyota en tête devant BMW et Ferrari (Alpine, Cadillac et Aston Martin groupés derrière).",
   "tables":[
     {"title":"Hypercar — Pilotes","rows":[
       {"p":1,"n":"Kobayashi / Conway / de Vries","sub":"Toyota #7","pts":75},{"p":2,"n":"Rast / Frijns","sub":"BMW","pts":71},
       {"p":3,"n":"van der Linde","sub":"BMW","pts":61},{"p":4,"n":"Hartley / Hirakawa / Buemi","sub":"Toyota #8","pts":56},
       {"p":5,"n":"Pier Guidi / Giovinazzi / Calado","sub":"Ferrari","pts":39},{"p":6,"n":"Félix da Costa / Milesi / Habsburg","sub":"Alpine","pts":28},
       {"p":7,"n":"Delétraz / Nato / Stevens","sub":"Cadillac","pts":26},{"p":8,"n":"Magnussen / Marciello","sub":"BMW","pts":25}]},
     {"title":"LMGT3 — Pilotes","rows":[
       {"p":1,"n":"Edgar / Catsburg","sub":"TF Sport · Corvette","pts":72},{"p":2,"n":"Keating","sub":"Corvette","pts":50},
       {"p":3,"n":"Rovera / Hériau / Mann","sub":"AF Corse · Ferrari","pts":40},{"p":4,"n":"David / van Rompuy","sub":"TF · Corvette","pts":37},
       {"p":5,"n":"Hawksworth","sub":"Lexus","pts":36}]}]},
 "elms": {"round":"après Le Castellet · 2/6","last":{"r":"4 H du Castellet","w":"United Autosports #22 (di Resta / Lindh / Goldburg)"},
   "note":"Pilotes LMP2 #22 : Paul di Resta, Rasmus Lindh, Dan Goldburg. Catégories : LMP2, LMP3, LMGT3.",
   "tables":[{"title":"LMP2 — Équipes","rows":[
     {"p":1,"n":"United Autosports","sub":"#22","pts":40},{"p":2,"n":"Inter Europol Competition","sub":"#34","pts":37},
     {"p":3,"n":"Forestier Racing by Panis","sub":"#29","pts":26}]}]},
 "gtwc": {"round":"après Brands Hatch · Spa en cours","last":{"r":"Circuit Paul Ricard","w":"Thiim / Drudi / Sørensen (Aston Martin)"},
   "note":"Classement général pilotes (overall). Spa, en cours ce week-end, n'est pas encore comptabilisé.",
   "tables":[{"title":"Pilotes (général)","rows":[
     {"p":1,"n":"Auer / Engel","sub":"Mercedes-AMG","pts":57},{"p":2,"n":"Stolz","sub":"Mercedes-AMG","pts":43},
     {"p":3,"n":"Thiim","sub":"Aston Martin","pts":34},{"p":4,"n":"Sørensen / Drudi","sub":"Aston Martin","pts":33},
     {"p":5,"n":"K. van der Linde / Weerts","sub":"BMW","pts":29},{"p":6,"n":"Pepper","sub":"Lamborghini","pts":25.5},
     {"p":7,"n":"Levi / Mazzola / Øgaard","sub":"Porsche","pts":25},{"p":8,"n":"Schuring / Boccolacci","sub":"Porsche","pts":24},
     {"p":9,"n":"Fleming / Prette","sub":"Ferrari","pts":21},{"p":10,"n":"Goethe","sub":"McLaren","pts":19}]}]},
 "dtm": {"round":"après le Lausitzring · 3/8","last":{"r":"Lausitzring (course 2)","w":"Matteo Cairoli (Ferrari)"},
   "note":"Équipes : Schubert Motorsport en tête (119), devant Emil Frey et Winward. Constructeurs : Mercedes-AMG en tête.",
   "tables":[{"title":"Pilotes","rows":[
     {"p":1,"n":"Cairoli","sub":"Emil Frey · Ferrari","pts":78},{"p":2,"n":"Engel","sub":"Winward · Mercedes","pts":77},
     {"p":3,"n":"Auer","sub":"Landgraf · Mercedes","pts":77},{"p":4,"n":"Wittmann","sub":"Schubert · BMW","pts":71},
     {"p":5,"n":"Dörr","sub":"Dörr · McLaren","pts":67},{"p":6,"n":"Thiim","sub":"Comtoyou · Aston Martin","pts":61}]}]},
 "wrc": {"round":"après le Japon · 7/14","last":{"r":"Rally du Japon","w":"Elfyn Evans (Toyota)"},
   "note":"Elfyn Evans en tête, +20 pts sur Katsuta ; Solberg 3e. Constructeurs : Toyota +93 sur Hyundai.",
   "tables":[{"title":"Pilotes","rows":[
     {"p":1,"n":"Elfyn Evans","sub":"Toyota","pts":None},{"p":2,"n":"Takamoto Katsuta","sub":"Toyota","pts":None},
     {"p":3,"n":"Oliver Solberg","sub":"Toyota","pts":None}]}]},
}

# GT World — pilotes (fiches officielles : id + slug réels)
gtwc_drivers = [
 {"pos":1,"n":"Lucas Auer","pts":57,"id":4102,"slug":"lucas-auer"},{"pos":1,"n":"Maro Engel","pts":57,"id":4145,"slug":"maro-engel"},
 {"pos":2,"n":"Luca Stolz","pts":43,"id":4146,"slug":"luca-stolz"},{"pos":3,"n":"Nicki Thiim","pts":34,"id":4057,"slug":"nicki-thiim"},
 {"pos":4,"n":"Marco Sørensen","pts":33,"id":4156,"slug":"marco-sorensen"},{"pos":4,"n":"Mattia Drudi","pts":33,"id":4155,"slug":"mattia-drudi"},
 {"pos":5,"n":"Kelvin van der Linde","pts":29,"id":4107,"slug":"kelvin-van-der-linde"},{"pos":5,"n":"Charles Weerts","pts":29,"id":4106,"slug":"charles-weerts"},
 {"pos":6,"n":"Jordan Pepper","pts":25.5,"id":4108,"slug":"jordan-pepper"},{"pos":7,"n":"Sebastian Øgaard","pts":25,"id":4084,"slug":"sebastian-ogaard"},
 {"pos":8,"n":"Morris Schuring","pts":24,"id":4053,"slug":"morris-schuring"},{"pos":9,"n":"Thomas Fleming","pts":21,"id":4096,"slug":"thomas-fleming"},
 {"pos":10,"n":"Benjamin Goethe","pts":19,"id":4141,"slug":"benjamin-goethe"},{"pos":11,"n":"Raffaele Marciello","pts":19,"id":4118,"slug":"raffaele-marciello"},
 {"pos":12,"n":"Jake Dennis","pts":19,"id":4119,"slug":"jake-dennis"},{"pos":13,"n":"Daniel Juncadella","pts":14,"id":4163,"slug":"dani-juncadella"},
 {"pos":14,"n":"Arthur Leclerc","pts":16.5,"id":4101,"slug":"arthur-leclerc"},{"pos":15,"n":"Valentino Rossi","pts":7.5,"id":4103,"slug":"valentino-rossi-"},
]

# Grille F1 (remplacée en live par Jolpica)
f1_teams = [
 {"t":"Mercedes","c":"#00D7B6","m":"AMG","d":[["Russell","🇬🇧","Britannique"],["Antonelli","🇮🇹","Italien"]]},
 {"t":"Ferrari","c":"#E8002D","m":"Ferrari","d":[["Leclerc","🇲🇨","Monégasque"],["Hamilton","🇬🇧","Britannique"]]},
 {"t":"McLaren","c":"#FF8000","m":"Mercedes","d":[["Norris","🇬🇧","Britannique"],["Piastri","🇦🇺","Australien"]]},
 {"t":"Red Bull Racing","c":"#3671C6","m":"Red Bull","d":[["Verstappen","🇳🇱","Néerlandais"],["Hadjar","🇫🇷","Français"]]},
 {"t":"Alpine","c":"#00A1E8","m":"Mercedes","d":[["Gasly","🇫🇷","Français"],["Colapinto","🇦🇷","Argentin"]]},
 {"t":"Racing Bulls","c":"#6692FF","m":"Red Bull","d":[["Lawson","🇳🇿","Néo-Zélandais"],["Lindblad","🇬🇧","Britannique"]]},
 {"t":"Haas","c":"#9CA3AF","m":"Ferrari","d":[["Bearman","🇬🇧","Britannique"],["Ocon","🇫🇷","Français"]]},
 {"t":"Williams","c":"#37BEDD","m":"Mercedes","d":[["Sainz","🇪🇸","Espagnol"],["Albon","🇹🇭","Thaïlandais"]]},
 {"t":"Audi","c":"#B0B4B8","m":"Audi","d":[["Hülkenberg","🇩🇪","Allemand"],["Bortoleto","🇧🇷","Brésilien"]]},
 {"t":"Aston Martin","c":"#229971","m":"Honda","d":[["Alonso","🇪🇸","Espagnol"],["Stroll","🇨🇦","Canadien"]]},
 {"t":"Cadillac","c":"#C7A14E","m":"Ferrari","d":[["Pérez","🇲🇽","Mexicain"],["Bottas","🇫🇮","Finlandais"]]},
]

seed = {
 "generated": datetime.datetime.utcnow().replace(microsecond=0).isoformat()+"Z",
 "source": "seed",
 "events": events,
 "standings": standings,
 "gtwcDrivers": gtwc_drivers,
 "f1Teams": f1_teams,
}

with open("seed_2026.json","w",encoding="utf-8") as fp:
    json.dump(seed, fp, ensure_ascii=False, indent=1)
print(f"seed_2026.json écrit : {len(events)} courses, {len(standings)} championnats, {len(gtwc_drivers)} pilotes GT World")
