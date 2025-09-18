# jenkins-flask-starter

Petit projet **Flask + tests PyTest** prêt pour **Jenkins Pipeline**. Deux pipelines fournis :

- `Jenkinsfile` : pipeline simple (tests + artefacts) – ne nécessite pas Docker côté Jenkins.
- `Jenkinsfile.docker` : pipeline complet (tests en conteneur + build d'image Docker + smoke test) – nécessite Docker accessible depuis l'agent Jenkins.

## Lancer l'app en local

```bash
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app/app.py  # http://localhost:5000/ping
```

## Lancer via Docker

```bash
docker build -t jenkins-flask-starter:local .
docker run --rm -p 5000:5000 jenkins-flask-starter:local
# puis http://localhost:5000/ping
```

## Utiliser avec Jenkins

1. Pousse ce dossier dans un dépôt Git (GitHub/GitLab).
2. Dans Jenkins → **New Item** → **Pipeline** → *Pipeline script from SCM* → collle l'URL Git.
3. Choisis le fichier `Jenkinsfile` (basique) ou `Jenkinsfile.docker` (avec build Docker).

### Si tu veux construire des images Docker dans Jenkins

- Si Jenkins tourne dans Docker (recommandé) : relance-le avec les montages suivants (Linux/macOS) :
  ```
  -v /var/run/docker.sock:/var/run/docker.sock
  -v /usr/bin/docker:/usr/bin/docker
  ```
- Sur Windows, fais tourner Jenkins dans WSL2 et applique les montages ci‑dessus, ou utilise un agent Linux séparé pour le build Docker.

Bon build !
