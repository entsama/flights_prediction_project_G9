# Prédiction des salaires dans les métiers de la data

Dans un monde de plus en plus axé sur les données, les professionnels de la data sont au cœur de nombreuses innovations technologiques et transformations numériques. 
Les métiers de la data, comprenant les data scientists, data analysts, data engineers, et autres, sont non seulement en forte demande mais aussi diversifiés en termes de compétences requises, responsabilités et, bien sûr, rémunérations. Ce projet vise à prédire les salaires dans les métiers de la data en se basant sur diverses caractéristiques professionnelles et personnelles.
Ce projet est une application web permettant de prédire les salaires des Data Scientists en fonction de divers paramètres tels que l'année de travail, le niveau d'expérience, le type d'emploi, etc.

# Objectifs Spécifiques
- Collecte de Données 
- Analyse Exploratoire des Données (EDA) 
- Modélisation Prédictive 
- Interprétation des Résultats 
- Développement d’un Outil Interactif 

# Méthodologie 
1 - Collecte et Préparation des Données :
  *Sources de données : https://ai-jobs.net/salaries/download/
  *Nettoyage des données : python

2- Analyse Exploratoire des Données (EDA) :
  *Visualisation des données : Power BI
3- Modélisation :
  *Sélection des modèles : Régression linéaire, Gradient Boosting
  *Validation des modèles 
  *Optimisation des hyperparamètres

4- Interprétation et Visualisation :
  *Importance des features 
  *Visualisation des prédictions : Graphiques interactifs pour comparer les prédictions aux données réelles.

5- Développement de l’Outil :
  *Interface utilisateur : Développement d’une application web ou d’un tableau de bord interactif.
  *Fonctionnalités : Entrée des caractéristiques utilisateur, affichage des prévisions salariales.

## Pour commencer

Nous avons récupéré nos données sur le site https://ai-jobs.net/salaries/download/

### Pré-requis

- Python 3.x
- Pip (gestionnaire de paquets pour Python)
- Un navigateur web moderne

### Installation

* Clonez le dépôt :
    Copier le code
    git clone https://github.com/votre-utilisateur/votre-repo.git
    cd votre-repo
* Installez les dépendances :
    Copier le code
    pip install -r requirements.txt
  
## Configuration

Préparez l'environnement :
 Assurez-vous d'avoir le fichier du modèle gb_model.joblib dans le répertoire racine du projet.

Structure des fichiers :

- app.py : Script principal pour lancer l'application Flask.
- data_loader.py : Script pour charger et traiter les données.
- train_model.py : Script pour entraîner le modèle.
- gb_model.joblib : Modèle de machine learning pré-entraîné.
- static/css/index.css : Fichier CSS pour le style de la page.
- static/js/index.js : Fichier JavaScript pour la logique du formulaire.
- templates/index.html : Fichier HTML pour l'interface utilisateur.

## Démarrage
Lancer l'application :
  bash
  Copier le code
  python app.py
Accédez à l'application :
Ouvrez votre navigateur web et allez à l'adresse suivante :
  arduino
  Copier le code
  http://localhost:5000
  
## Utilisation
Remplissez le formulaire :
Sur la page d'accueil, remplissez le formulaire avec les informations requises (année de travail, niveau d'expérience, type d'emploi, etc.).

Soumettez le formulaire :
Cliquez sur le bouton "Prédire le Salaire" pour obtenir la prédiction de salaire.

## Voir le résultat :
Le résultat s'affichera en dessous du formulaire, montrant le salaire prédit.

## Technologies utilisées 

Les programmes/logiciels/ressources que nous avons utilisés pour développer notre projet

* [Excel](https://www.microsoft.com/fr-fr/microsoft-365/excel) - Excel
* [Power BI](https://www.microsoft.com/fr-fr/power-platform/products/power-bi) - Power BI
* [Power BI](https://code.visualstudio.com/Visual) - Visual studio code
* [Flask](https://flask.palletsprojects.com/en/3.0.x/) - Flask
* [Flask](https://www.mongodb.com/fr-fr) - MongoDB
* [Flask](https://www.postman.com/) - Postman

## Architecture
- Data sources : https://ai-jobs.net/salaries/download/ , Cette source de données nous a permi de télécharger des ensembles de données sur les salaires dans le domaine de l'intelligence artificielle. 
- BI : Power BI, outil de business intelligence qui nous a permis de visualiser et d'analyser les données. 
- Data preparation : Mongodb c'est la base de données NoSQL utilisée pour stocker des données non structurées ou semi-structurées. VS Code, éditeur de code léger et puissant qui supporte de nombreux langages de programmation. Python, langage de programmation polyvalent très utilisé en data science pour la manipulation des données, l'analyse statistique, et le développement de modèles de machine learning. 
- AI Machine / Machine learning: Après avoir testé d'autres modèles dont la régression linéaire, nous avons choisi le modèle Gradient boosting, c'est une technique de machine learning utilisée pour les problèmes de régression et de classification. Il construit un modèle prédictif en combinant plusieurs modèles plus simples (comme les arbres de décision) de manière séquentielle pour corriger les erreurs des modèles précédents, ce qui améliore la précision en terme de prediction des salaires.
- Interface : Flask, qui est un micro-framework web en Python qui nous a permis de développer l'interface web. Il est utilisé pour créer des interfaces utilisateur, des API RESTful et pour servir le modèle de machine learning dans une application web.

##  Comparaison avec les autres modèles étudiés 



## Impact du Projet
Ce projet apportera une valeur significative aux professionnels de la data, aux recruteurs et aux entreprises en fournissant une vision claire et précise des tendances salariales. Il aidera les individus à mieux négocier leurs salaires et les employeurs à structurer des offres compétitives et équitables.
Avec une approche méthodique et axée sur les données, ce projet contribuera à une meilleure compréhension du marché du travail dans les métiers de la data, facilitant ainsi une prise de décision informée pour tous les acteurs concernés.

## Contribution
Les contributions sont les bienvenues ! Veuillez créer une pull request ou ouvrir une issue pour discuter des changements que vous souhaitez apporter.

## Versions
Listez les versions ici 
_exemple :_
**Dernière version stable :** 5.0
**Dernière version :** 5.1
Liste des versions : [Cliquer pour afficher](https://github.com/your/project-name/tags)
_(pour le lien mettez simplement l'URL de votre projets suivi de ``/tags``)_

## Auteurs
Les auteurs du projet sont :
* **Mamakan COULIBALY** : Responsable technique (focalisée sur la recherche de l'API, la configuration des environnements, et les spécifications techniques).
* **Estelle NTSAMA** : Responsable de la gestion de projet et de la coordination (supervisation de toutes les tâches, participation à la rédaction du plan et des spécifications).
* **Ulukbek OMOEV** : Responsable des données et de l'intégration (focalisé sur la documentation de l'API, les premières requêtes, et la préparation des données).

## License
Ce projet a été réalisé dans le cadre d'un devoir académique !


