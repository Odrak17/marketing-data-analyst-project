 # marketing-data-analyst-project


# Contexte du projet: 
Avant tout il sied de signaler que le dataset sur lequel porte notre travail a été téléchargé sur Maven Analytics à des fins d'apprentissage. Ce projet  d'analyse de données est un projet dans le secteur marketing qui vise à comprendre les comportements des clients et la performance des différentes campagnes marketing.

# Objectifs du projet
Notre projet s'articule autour des objectifs suivants:
 - Evaluer la qualité des données 

 - Analyse des facteurs influençant les achats en ligne 

 - Mesurer la performance des campagnes marketing 

 - Définir le profil du client moyen 

 - Analyser la performance des produits 

 - Évaluer les canaux marketing 

# Missions du projet :
Dans le but d'atteindre les différents objectifs, les missions suivantes ont été définies :
* Objectif 1 : Evaluer la qualité des données 
- Identifier les anomalies sur les données (valeurs manquantes, les outliers, doublons,...)
- Définir des règles de nettoyage et de traitement  adaptées.
- Appliquer les règles définies

* Objectif 2 : Analyse des facteurs influençant les achats en ligne
- Gatégoriser  les potentielles variables explicatives en leur type approprié(numérique,catégorielle,string,booléennes).
- Faire une analyse univariée (analyser chaque variable suspectée explicative de la variable cible)
- Faire une analyse bivariée (Chaque variable explicative vs variable civle)
- Mettre en évidence les variables les plus influentes sur les achats

* Objectif 3 : Mesurer la performance des campagnes marketing 
- Analyser les taux d’acceptation des différentes campagnes
- Comparer les performances des campagnes marketing
- Identifier les profils clients les plus réceptifs aux campagnes

* Objectif 4 : Définir le profil du client moyen 
- Analyser les caractéristiques démographiques des clients
- Étudier les comportements d’achat dominants
- Construire un profil type du client moyen

* Objectif 5 : Analyser la performance des produits
- Identifier les produits générant le plus de revenus
- Comparer les volumes d’achat par catégorie de produits
- Mettre en évidence les produits sous-performants et performants

* Objectif 6 :  Évaluer les canaux marketing 
- Analyser la performance des différents canaux d’acquisition
- Identifier les canaux les plus et les moins efficaces
- Formuler des recommandations stratégiques

# Présentation du jeu de données :
    Le jeu de données contient 2240 clients(lignes) et 28 colonnes. Il renseigne sur les informations des clients ainsi que leurs différentes réponses aux différents campagnes marketing

# Approches :

# Fonctionnalités / Particularités du projet :

# Outils : 
    Github : 
    Python :
    Power Bi :

# Présentation des résultats
* Objectif 1 : Dans l'évalution de la qualité des données, nous avons remarqué sans grande surprise que le dataset présente des anomalies et les avons traitées via des règles bien définies qui nous détaillerons ci-dessous.
- Avant d'aller plus loin il sied de signaler que les différentes colonnes ont été traduites de l'anglais en français pour une meilleure compréhension du jeu de données.

- Problème de typage concernant certaines colonnes:
    - Les différentes colonnes représentant les différentes campagnes marketing, les réponses et plaintes étaient de type int. Nous les avons donc converties en type bool.

    - La colonne Date_Inscription était de type object, qui n'est son type approprié et peut induire en erreur dans certaines opérations. Nous l'avons convertie en type date.

- Absence de la variable Age : Le dataset ne contenait que la colonne qui référençait l'année de naissance de chaque client. Conscient que le cerveau humain manipule mieux l'âge que l'année, et que nous travaillons sur des activités enregistrées de 2012 à 2014, nous avons créé une colonne âge en considérant 2014 comme année actuelle.

- Incohérences de certaines  modalités.
    - La colonne référençant le niveau d'éducation de chaque client contenait la modalité 'Graduate', ce qui est incohérent,suggérant une possible erreur de saisie suivi d'une duplication du mauvais terme. Nous l'avons remplacé par Graduation qui est correct et proche de Graduate.

    - S'agissant de la colonne représentant le statut matrimonial de chaque client, nous avons remarqué deux modalités 'YOLO' et 'Absurd' qui n'ont totalement aucun rapport avec le statut matrimonial. Leur faible présence dans la colonne Statut_Marital(au total 4/2240) nous a permis de les supprimer. 

    - Nous avons aussi remarqué la modalité 'Alone' qui n'est pas un statut matrimonial. Nous l'avons fusionnée à la modalité 'Single' car leur sens est très proche. 
    
    - S'agissant de la modalité 'Together' qui n'est pas un statut matrimonial, nous l'avons fusionnée à 'Married' en raison de leur approximité.

- Il sied de signaler qu'en depit de certaines anomalies présentées, le dataset ne présente aucun doublon.

- S'agissant des valeurs manquantes :
    - Seul la colonnes Revenu présentait des valeurs manquantes, précisément 24 valeurs manquantes(soit 0,01% de la colonne revenu). 

    - Avant tout traitement, nous avons pu identifié que les valeurs manquantes sont de type MAR et avons procédé à une imputation conditionnnelle par la médiane en fonction des catégories des nombre d'enfants.

- S'agissant des valeurs aberrantes:
     - Nous avons regroupé les variables référençant les différents montants(Montant_Fruits,Montant_Or,...) dépensés en une seule variable, autant pour les différents nombre d'achat selon leur canal(Nb_SiteWeb, NbAchat_Magasin,...) afin de ne pas considérer comme abberrant la préférence d'un client. 

     - La colonne "Nbjour_Dernier_Achat" n'a présenté aucune valeur aberrante
     
     - Les colonnes("Revenu","Montant_Total","Age", "NbAchat_Total", ) ont présenté des valeurs aberrantes proches de l'intervalle défini. Celle qui a attiré notre attention est la colonne "Revenu" avec une valeur aberrante extrême qui est 666666 . Nous aurions pu l'assimiler à un client premium mais son très faible pouvoir d'achat nous a fait rejetté cette hypothèse. En raison de sa faible proportion dans le revenu(0,0004%), nous avons donc supprimé cette valeur aberrante car elle s'écarte largement de la réalité d'un client de compagnie. 
     
     - Aussi toutes les valeurs aberrantes proches de l'intervalle définie n'ont pas été traitées car qui dit valeur aberrante ne dit pas forcément anomalie, de même celles-ci se rapprochent de la tendance des différentes variables et il faut noter que certains clients ont un pouvoir d'achat assez conséquent et une forte préférence pour certains produits et canal d'achat. 
     
    - Conernant la variable âge nous avons détecté 114, 115 et 121 qui ne sont pas plausibles. En raison de leur faible proportion dans la colonne âge, nous avons décidé de les supprimer.

- Après traitement des anomalies du dataset brut, il a été exporté en fichier .csv afin de contribuer à l'atteinte des objectifs fixés.

* Objectif 2: