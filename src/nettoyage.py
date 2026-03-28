# Dans ce fichier, sont défnies toutes les fonctions utiles pour le nettoyage des données

#Importation des bibliothèques
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats


#Fonction pour trouver les valeurs aberrantes dans chaque variables numérique d'un dataset
#Analyse statistique: Détection des valeurs aberrantes avec l'approche de l'IQR
def valeur_aberrante(df,colonne):
    if colonne in df.select_dtypes(include="number").columns:
        valeur=df[colonne].sort_values(ascending=True)
        q1=valeur.quantile(0.25)        #ou q1=np.percentile(valeur, 25)
        q2=valeur.quantile(0.50)        #ou q2=np.percentile(valeur,50)
        q3=valeur.quantile(0.75)        #ou q3=np.percentile(valeur,75)
        iqr=q3-q1
        born_inf=q1-1.5*iqr
        born_sup=q3+1.5*iqr
        aberrantes=valeur[(valeur < born_inf) | (valeur> born_sup) ]
        print(f"----- {colonne} -----")
        print(f"Minimum:{df[colonne].min()}")
        print(f"Maximum:{df[colonne].max()}")
        print(f"Q1 = {q1}, Q2 = {q2}, Q3 = {q3}")
        print(f"Borne inférieure = {born_inf}, Borne supérieure = {born_sup}")
        if aberrantes.empty:
            print("Aucune valeur aberrante détectée.")
        else:
            print(f"le nombre de valeurs aberrantes est :{aberrantes.count()}\n")
            print("Valeurs aberrantes détectées :")
            print(aberrantes.to_string(index=False))
        print("\n")
    else :
        print(f"Les valeurs aberrantes n'existent que pour les variables de type numérique")