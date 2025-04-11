# 🚀 FastAPI Notification API

API de gestion de notifications construite avec FastAPI (Python 3.7+)

## 📦 Installation locale

```bash
# 1. Cloner le projet
git clone https://github.com/votre-user/fastapi-notif.git
cd fastapi-notif

# 2. Créer l'environnement virtuel
python -m venv venv
source venv/bin/activate  # Linux/MacOS
# .\venv\Scripts\activate  # Windows

# 3. Installer les dépendances
pip install -r requirements.txt

# 4. Lancer le serveur (dev)
uvicorn app.main:app --reload

```

## 🌐 Accès à l'API

**Local**  
🔗 http://localhost:8000

**Production**  
🔗 https://fastapi-slev.onrender.com

## 📡 Endpoints

### PUT /notifications/
Reçoit une notification

**Requête :**
```json
{
  "status": "completed",
  "serverCorrelationId": "bf37cfff-0bb7-4dd1-8c1e-1b46bda2f59d",
  "notificationMethod": "callback",
  "objectReference": "932151316"
}
```


### PUT /notifications/
Reçoit une notification

**Exemple de réponse :**
```json
{
  "serverCorrelationId": "bf37cfff-0bb7-4dd1-8c1e-1b46bda2f59d",
  "received_at": "2023-04-10T12:34:56.789Z"
}
```
### GET /notifications/{serverCorrelationId}
**Description** : Liste toutes les notifications reçues  
**Méthode** : GET  
**Réponse** :
```json
[
  {
    "id": 1,
    "status": "completed",
    "serverCorrelationId": "bf37cfff-0bb7-4dd1-8c1e-1b46bda2f59d",
    "received_at": "2023-04-10T12:34:56.789Z"
  },
  {
    "id": 2,
    "status": "pending",
    "serverCorrelationId": "a1b2c3d4-5678-90ef-ghij-klmnopqrstuv",
    "received_at": "2023-04-11T08:15:22.123Z"
  }
]
```
## 🏗 Structure du projet

```
.
├── app/
│ ├── init.py # Initialisation du module
│ ├── main.py # Configuration principale FastAPI
│ ├── models.py # Modèles de données (SQLAlchemy ORM)
│ ├── schemas.py # Validation des données (Pydantic)
│ └── database.py # Configuration de la base de données
│
├── tests/ # Tests automatisés
│ ├── init.py
│ └── test_api.py # Tests des endpoints
│
├── .env # Configuration d'environnement
├── .gitignore # Fichiers exclus du versioning
├── requirements.txt # Dépendances Python
└── README.md # Documentation du projet

```
## 🛠 Roadmap

### Prochaines fonctionnalités
- [ ] **Authentification JWT**
  - Sécurisation des endpoints
  - Gestion des rôles
  - Tokens d'accès/rafraîchissement
- [ ] **Gestion des erreurs améliorée**
  - Messages d'erreur standardisés
  - Codes HTTP précis
  - Logging des erreurs
- [ ] **Couverture de tests**
  - Tests unitaires (90%+)
  - Tests d'intégration
  - Tests de performance
- [ ] **Système de logging**
  - Fichiers de logs journaliers
  - Niveaux de log (DEBUG, INFO, ERROR)
  - Rotation automatique

## 📜 Licence

**MIT License**  
Copyright (c) 2023 [Votre Nom/Votre Organisation]

Permission est accordée, gracieusement, à toute personne obtenant une copie de ce logiciel et des fichiers de documentation associés de traiter le Logiciel sans restriction, y compris sans limitation les droits d'utiliser, copier, modifier, fusionner, publier, distribuer, sous-licencier et/ou vendre des copies du Logiciel.