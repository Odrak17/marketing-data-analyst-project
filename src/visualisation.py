import pandas as pd
import numpy as np
import seaborn as sns 
import scipy.stats as stats
import matplotlib.pyplot as plt



#fonction pour visualiser le boxplot d'une variable de type numérique
def graphe_boxplot(df:pd.DataFrame,col:str):
    if col in df.select_dtypes(include="number").columns:
        sns.boxplot(x=df[col]) #Boxplot horizental
        plt.figure()
        plt.title(f"Boxplot de {col}")
        plt.show()



#fonction pour visualiser l'histplot et le kdeplot d'une variable de type numérique
def graphe_histplot(df:pd.DataFrame,col:str):
    if col in df.select_dtypes(include="number").columns:
        plt.figure()
        sns.histplot(x=df[col],kde=True) #Boxplot horizental
        plt.title(f"Histplot de {col}")
        plt.show()


#Fonction pour visualiser le boxplot d'une variable numérique en fonction d'une variable catégorielle ou booléenne
def graphe_box(df:pd.DataFrame,col1:str, col2:str):
    if (col1 in df.select_dtypes(include="number").columns) and (col2 in df.select_dtypes(include=["object","string"]).columns):
        plt.figure()
        sns.boxplot(x=df[col1],y=[col2]) #Boxplot horizental
        plt.title(f"Boxplot de {col1} en fonction de {col2}")
        plt.show()