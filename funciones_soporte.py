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
    return df_reporte