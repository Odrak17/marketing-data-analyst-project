# Dans ce fichier, sont définies les fonctions portant sur les tests statistiques nécessaires au projet

#Importation des bibliothèques
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats


"""Test de shapiro-Wilk. Ce test permet de vérifier si les données de type numérique suivent la loi normale. Il prend en compte toutes les
données numériques du dataset. Il suffit d'entrer en paramètre un dataset donné"""

def test_shapiro(df):
    for var in df.select_dtypes(include='number').columns:
        stat_test, p=stats.shapiro(df[var])
        print(f"{var}\n")
        if p>0.05 :
            print(f"Les données suivent la loi normale\n") #L"hypothèse H0 est acceptée 
        else:
            print(f"Les données ne suivent par la loi normale\n")   #L'hypothèse H0 est rejettée


# Test de contingence pour tester la dépendance entre deux variables catégorielles
def test_contingence(df,col1, col2): #col1  désigne la colonne contenant les valeurs manquantes et col2 désigne toute colonne catégorielle suspectée d'être en relation avec col1
    if df[col1].isna().any():
        df["Manquants"]=df[col1].isna()
        table=pd.crosstab(df[col2],df["Manquants"])
        chi2, p, dof, expected=stats.chi2_contingency(table) #chi2: Statistique de test; p:p-value; dof:degré de liberté; expected : Effectif théorique
        print(f"----------{col2}------------\n")
        print(f"{table}\n")
        print(f"Statistique de khi-2:{chi2}\n")
        print(f"p-value: {p}\n")
        if p>0.05:
            print(f"Pas de relation significative avec les valeurs manquantes\n") #L"hypothèse H0 est acceptée
        else:
            print(f"Relattion significative avec les valeurs manquantes\n") #L'hypothèse H0 est rejettée




