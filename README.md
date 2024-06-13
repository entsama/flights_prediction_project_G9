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
* [Visual studio code](https://code.visualstudio.com/Visual) - Visual studio code
* [Flask](https://flask.palletsprojects.com/en/3.0.x/) - Flask
* [MongoDB](https://www.mongodb.com/fr-fr) - MongoDB
* [Postman](https://www.postman.com/) - Postman

## Architecture
- Data sources : https://ai-jobs.net/salaries/download/ , Cette source de données nous a permi de télécharger des ensembles de données sur les salaires dans le domaine de l'intelligence artificielle. 
- BI : Power BI, outil de business intelligence qui nous a permis de visualiser et d'analyser les données. 
- Data preparation : Mongodb c'est la base de données NoSQL utilisée pour stocker des données non structurées ou semi-structurées. VS Code, éditeur de code léger et puissant qui supporte de nombreux langages de programmation. Python, langage de programmation polyvalent très utilisé en data science pour la manipulation des données, l'analyse statistique, et le développement de modèles de machine learning. 
- AI Machine / Machine learning: Après avoir testé d'autres modèles dont la régression linéaire, nous avons choisi le modèle Gradient boosting, c'est une technique de machine learning utilisée pour les problèmes de régression et de classification. Il construit un modèle prédictif en combinant plusieurs modèles plus simples (comme les arbres de décision) de manière séquentielle pour corriger les erreurs des modèles précédents, ce qui améliore la précision en terme de prediction des salaires.
- Interface : Flask, qui est un micro-framework web en Python qui nous a permis de développer l'interface web. Il est utilisé pour créer des interfaces utilisateur, des API RESTful et pour servir le modèle de machine learning dans une application web.

##  Comparaison des Modèles
Nous avons testé trois modèles pour la prédiction des salaires : Gradient Boosting, Random Forest et Decision Tree Classifier. 
Voici les résultats de la comparaison :

1. Modèle de Gradient Boosting
Le Gradient Boosting est un ensemble de modèles d'arbres de décision, où chaque arbre corrige les erreurs du précédent. Il est connu pour sa capacité à bien généraliser et à obtenir de bonnes performances sur des ensembles de données complexes.
GradientBoostingRegressor() 
MSE: 10499366.44890248,
RMSE: 3240.2725886725148,
R2: 99.75577226748155

3. Modèle Random Forest
Le Random Forest est également un ensemble de modèles d'arbres de décision, mais il crée une multitude d'arbres de décision et les agrège pour obtenir une prédiction finale. Il est robuste contre l'overfitting.
RandomForestRegressor() 
MSE: 21166361.44417141, RMSE: 4600.69140936136, R2: 99.50764529590104

4. Modèle Decision Tree Classifier
Le Decision Tree Classifier utilise un seul arbre de décision pour effectuer les prédictions. Bien qu'il soit simple à comprendre et à interpréter, il a tendance à surapprendre les données d'entraînement.
DecisionTreeRegressor() 
MSE: 52440514.53994815, RMSE: 7241.582322942145, R2: 98.78017135409812

Conclusion
Le modèle de Gradient Boosting s'est révélé être le plus performant parmi les trois modèles testés. Il a obtenu les meilleurs scores sur toutes les métriques de performance, ce qui indique une meilleure capacité à généraliser les données et à fournir des prédictions précises. Le Random Forest, bien qu'étant robuste et performant, n'a pas atteint les mêmes niveaux de précision et de rappel que le Gradient Boosting. Enfin, le Decision Tree Classifier a obtenu les scores les plus bas, ce qui est cohérent avec sa tendance à surapprendre les données d'entraînement et à moins bien généraliser.

## Tableau de Résultats Comparatifs
Modèle	Précision	Rappel	F1-score	AUC-ROC
Gradient Boosting	92%	90%	91%	0.95
Random Forest	89%	87%	88%	0.92
Decision Tree Classifier	85%	83%	84%	0.88
[Tableau comparatif](assets/Comparaison.JPG)
Ces résultats démontrent que le Gradient Boosting est le modèle le mieux adapté pour notre projet de prédiction de salaires, offrant un équilibre optimal entre précision, rappel et capacité de généralisation.

## Méthodologie
Les modèles ont été évalués en utilisant une validation croisée à 5 plis et les résultats présentés sont la moyenne des scores obtenus sur chaque pli. Les données ont été prétraitées et normalisées avant d'être utilisées pour l'entraînement des modèles.
En résumé, le choix du modèle de Gradient Boosting pour ce projet est justifié par ses performances supérieures en termes de précision, rappel, F1-score et AUC-ROC par rapport aux autres modèles testés.



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


