# Para tratamiento de datos
import numpy as np
import pandas as pd
# Para visualizaciones
import seaborn as sns 
import matplotlib.pyplot as plt
# Para generar todas las combinaciones posibles
import itertools
# Para guardar DataFrames en Excel
from pandas import ExcelWriter
# Para gestión de fechas
from datetime import datetime
# Ignorar warnings
import warnings
warnings.filterwarnings("ignore")
# Configuración para poder visualizar todas las columnas de los DataFrames
pd.set_option('display.max_columns', None) 



## definimos una función que nos genere un reporte
def reporte(df):
    df_reporte = pd.DataFrame()
    df_reporte["valores_nulos"] = df.isnull().sum()
    df_reporte["porcentaje_nulos"] = round(((df.isnull().sum())/df.shape[0])*100,2)
    df_reporte["tipo_dato"]=df.dtypes
    df_reporte = df_reporte.reset_index(drop=False)
    return df_reporte


def reemplazar(df, columnas, viejo, nuevo):
    """Reemplaza un valor en un string por uno nuevo para una lista de columnas de un dataframe

    Args:
        df (dataframe): dataframe al que pertenecen las columnas que queremos cambiar
        columnas (list): lista de columnas del dataframe en las que queramos aplicar el cambio
        viejo (str): patrón que queremos sustituir
        nuevo (str): patrón nuevo que queremos que aparezca

    
    Returns:
        Dataframe con los reemplazos hechos
    """
    for columna in columnas:
        df[columna] = df[columna].str.replace(viejo, nuevo)
    return df