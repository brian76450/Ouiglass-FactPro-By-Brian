# OUIGLASS FACTPRO V4 By BRIAN

## Description
OUIGLASS FACTPRO est un logiciel de gestion hypermoderne conçu pour S.A.S Normandie Vitrages. Il inclut des fonctionnalités avancées pour gérer les clients, factures, services, stock, et analytiques.

## Fonctionnalités
- **Page de lancement** : Design futuriste et dynamique.
- **Page de connexion** : Authentification par code à 4 chiffres avec gestion des rôles.
- **Dashboard** : Modules interactifs pour clients, factures, services, stock, et analytiques.
- **Notifications** : Système de notifications dynamiques.
- **Rapports analytiques** : Graphiques interactifs et exportation au format PDF.
- **Mode sombre** : Option pour basculer entre mode clair et sombre.
- **Mobile-friendly** : Interface adaptée pour les appareils mobiles.

## Installation
1. Clonez le dépôt ou copiez les fichiers dans un dossier local.
2. Activez l'environnement virtuel :
   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```
3. Installez les dépendances :
   ```powershell
   pip install -r requirements.txt
   ```

## Exécution
1. Lancez l'application Flask :
   ```powershell
   python dashboard.py
   ```
2. Accédez à l'application via :
   ```
   http://127.0.0.1:5000/
   ```

## Structure du projet
- `dashboard.py` : Fichier principal pour gérer les routes.
- `database.py` : Gestion de la base de données SQLite.
- `templates/` : Fichiers HTML pour les pages.
- `static/` : Fichiers CSS et autres ressources.

## Auteur
**Brian**

## Informations de l'entreprise
S.A.S Normandie Vitrages  
RD 926 - 94 rue Nizas - Fauville-en-Caux  
76640 TERRES-DE-CAUX  
Téléphone : 02.35.16.29.26  
SIRET : 835 336 314 00025
