# Gmail API Email Processor 📧

Un outil puissant pour automatiser le traitement des emails via l'API Gmail avec des fonctionnalités avancées de classification et d'étiquetage.

![Gmail API](https://img.shields.io/badge/Gmail_API-1.0.0-blue) ![Python](https://img.shields.io/badge/Python-3.8%2B-green)

## ✨ Fonctionnalités principales

- **Authentification sécurisée** : 
  - Intégration OAuth2 avec gestion automatique des tokens
  - Support multi-compte (configuration facile)
  
- **Traitement intelligent des emails** :
  - Filtrage avancé par requêtes personnalisables
  - Classification automatique par catégories
  - Gestion des labels (création, application, suppression)
  
- **Support international** :
  - Interface multilingue (FR/EN)
  - Prise en charge des caractères spéciaux

## 📋 Prérequis

- Python 3.8+
- Compte Google avec accès API activé
- Projet configuré dans [Google Cloud Console](https://console.cloud.google.com/)

## 🚀 Installation rapide

1. Cloner le dépôt :
```bash
git clone https://github.com/votre-repo/gmail-api-email-processor.git

cd gmail-api-email-processor
```
    Installer les dépendances :
pip install -r requirements.txt
```

    Configurer les credentials :

        Créer un projet dans Google Cloud Console

        Activer l'API Gmail

        Générer des credentials OAuth 2.0 (type "Application de bureau")

        Télécharger le fichier credentials.json dans le dossier du projet
