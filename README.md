# PITWALL 🏁

Calendrier perso multi-séries (F1, WEC, ELMS, GT World Challenge, DTM, WRC) — PWA installable sur iPhone et ordi, hébergée sur GitHub Pages. Horaires en heure française, classements, derniers résultats, fiches pilotes, export agenda, favoris.

## Les fichiers

| Fichier | Rôle |
|---|---|
| `index.html` | L'app (tout-en-un). C'est elle que sert GitHub Pages. |
| `data.json` | Les données affichées. **Produit par le robot** — ne pas éditer à la main. |
| `seed_2026.json` | La base vérifiée. Le robot part de là. |
| `fetch_data.py` | **Le robot.** Récupère la F1 en direct, fusionne, écrit `data.json`. |
| `build_seed.py` | Régénère `seed_2026.json` (si tu veux corriger une donnée de base). |
| `.github/workflows/update-data.yml` | Lance le robot chaque jour, automatiquement. |

## Mise en ligne (une seule fois)

1. Crée un dépôt GitHub (ex. `pitwall`) et **dépose tous les fichiers** en gardant l'arborescence (le dossier `.github/workflows/` doit rester tel quel).
2. **Settings → Pages** : Source = branche `main`, dossier `/root`. Ton app est en ligne à `https://<ton-pseudo>.github.io/pitwall/`.
3. **Settings → Actions → General → Workflow permissions** : coche **Read and write permissions** (pour que le robot puisse publier `data.json`).
4. Onglet **Actions → Mise à jour des données PITWALL → Run workflow** pour un premier lancement immédiat. Ensuite il tourne tout seul chaque jour.

Sur iPhone : ouvre l'URL dans Safari → Partager → **Ajouter à l'écran d'accueil**.

## Comment marche le robot

- **F1** : récupérée en direct via l'**API ouverte Jolpica** (successeur d'Ergast) — calendrier, horaires de séances, vainqueurs, classements pilotes & constructeurs. Sans clé, gratuit.
- **WEC / ELMS / GTWC / DTM / WRC** : à partir des données vérifiées de la graine (pas d'API ouverte). L'app n'est jamais cassée : si une source tombe, le robot garde la graine.
- L'app recharge `data.json` au lancement (et toutes les 30 min). Si le fichier manque, elle utilise la graine intégrée → elle marche toujours, même hors-ligne.

## Étendre l'auto-mise-à-jour aux autres séries

Dans `fetch_data.py`, ajoute une fonction `update_<serie>(data)` sur le modèle de `update_f1()`. Sources confirmées lisibles par machine :

- **GTWC** : `gt-world-challenge-europe.com/standings`, `/drivers`, fiches `/driver/<id>/<slug>` (avec photos) — déjà testé, ça se lit.
- **ELMS** : timing Al Kamel (`elms.alkamelsystems.com`) — JSON + PDF.
- **DTM** : `dtm.com/en/results` et standings.
- **WEC** : `fiawec.com`.
- **WRC** : `wrc.com` (live timing partenaire).

Les pages rendues côté navigateur (GTWC, DTM…) nécessitent un rendu headless (Playwright) à ajouter dans le workflow. C'est la prochaine brique : import natif des fiches pilotes complètes (photo, date de naissance, palmarès, réseaux) et des résultats détaillés (qualifs, incidents).
