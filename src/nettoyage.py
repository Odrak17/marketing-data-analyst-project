# Dans ce fichier, sont défnies toutes les fonctions utiles pour le nettoyage des données

#Importation des bibliothèques
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats


#Fonction pour trouver les valeurs aberrantes dans chaque variables numérique d'un dataset
#Analyse statistique: Détection des valeurs aberrantes avec l'approche de l'IQR
def valeur_aberrante(df:pd.DataFrame,colonne:str):
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
    return


""" La fonction ci-dessous permet de mesurer le taux d'asymétrie et de vérifier si une transformation est possible"""

def asymetrie(df:pd.DataFrame,col:str):
    if col in df.select_dtypes(include="number"):
        print(f"-----------{col}--------\n")
        coeff_asy=df[col].skew()
        print(f"Coéfficient d'asymétrie : {coeff_asy}\n")
        if coeff_asy<1:
            print(f"Nature de la distribution : négativement asymétrique\n")
        elif coeff_asy==1:
            print(f"Nature de la distribution : Symétrique\n")
        else :
            print(f"Nature de la distribution : positivement asymétrique\n")
        if abs(coeff_asy)<0.5:
            print(f"Note : La distribution est légèrement asymétrique. Pas de transformation nécessaire")
        elif abs(coeff_asy)<1:
            print(f"Note : La distribution est modéremment symétrique. Une transformation est optionnelle")
        else :
            print(f"Note : La distribution est fortement symétrique. Une transformation est primordiale")



"""La fonction ci-dessous est une fonction qui permettra d'appliquer une transformation logarithmique
via numpy afin de reduire l'impact des outliers sur une variable donné et minimiser le risque de biais.
Elle permet de rapprocher les données de la normalité et est applicable pour les données fortement asymétriques.
Cette transformation est agressive"""

def transform_log(df:pd.DataFrame,col:str):
    df[f"{col}_transformlog"]=np.log1p(df[col]) #nplog1p(x)=nplog(x+1) permet d'éviter les valeurs nulles 
    print(f"----------{col}_transformlog-------------")
    print(df[f"{col}_transformlog"])
    return


"""La fonction ci-dessous est une fonction qui permettra d'appliquer une transformation racine carrée via numpy afin de reduire 
l'impact des outliers sur une variable donné et minimiser le risque de biais.Elle permet de rapprocher les données de la normalité 
et est applicable pour les données fortement asymétriques. Elle est une transformation douce"""

def transform_sqrt(df:pd.DataFrame,col:str):
    df[f"{col}_sqrt"]=np.sqrt(df[col]) 
    print(f"----------{col}_sqrt-------------")
    print(df[f"{col}_sqrt"])
    return


""" La fonction ci-dessous permet d'appliquer la winorisation, c'est-à-dire remplacer les valeurs extrêmes par des valeurs
limites"""

def capping(df,col):
    inf=df[col].quantile(0.01)
    sup=df[col].quantile(0.99)
    df[f"{col}_capped"]=df[col].clip(inf,sup)
    print(f"{col}_capped")
    print(df[f"{col}_capped"])
    return




