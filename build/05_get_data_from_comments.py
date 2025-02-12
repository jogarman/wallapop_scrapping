#!/usr/bin/env python
# coding: utf-8

# Extrae el % de bateria del comentario y lo pega en la columna de bateria

# In[1]:


import pandas as pd
import re
from datetime import datetime


# In[ ]:


elemento_a_buscar = "iphone"

carpeta = "../data/4_download_description"
fecha = datetime.now().strftime("%Y%m%d")
#fecha = "20250117"


# In[3]:


nombre_archivo = fecha + '_' + elemento_a_buscar
df_original = pd.read_csv(carpeta + '/' + nombre_archivo + '.csv')
df_original.drop('Unnamed: 0', axis=1, inplace=True)
df_original.head(2)


# In[4]:


df = df_original.copy()


# In[5]:


def encontrar_bateria(texto: str):
    # Verificar si el texto es NaN o similar
    if pd.isna(texto):
        return None
    # Buscar números seguidos por %
    numeros_con_porcentaje = re.findall(r'\b(8[0-9]|9[0-9]|100)\b%', texto)
    # Si encuentra números con %, devolver el primero
    if numeros_con_porcentaje:
        return numeros_con_porcentaje[0] 
    # Si no hay % buscar solo los números
    numeros = re.findall(r'\b(8[0-9]|9[0-9]|100)\b', texto)
    # Si encuentra números, devolver el primero
    if numeros:
        return numeros[0]
    # Si no encuentra ningún número, devolver None
    return None


# In[6]:


# buscar 128|256|512 seguido de \s*(Mb|MB|mb)
# si no, buscar \b1[Tt]\b
# si no, buscar \b(128|256|512)\b
def encontrar_memoria(texto: str) -> str:
    if pd.isna(texto):
        return None
    texto = str(texto)
    
    # Buscar 128|256|512 seguido de \s*(Mb|MB|mb)
    memorias_con_unidades = re.search(r'\b(128|256|512)\b\s*(Mb|MB|mb)', texto)
    if memorias_con_unidades:
        memoria, unidad = memorias_con_unidades.groups()
        return memoria + unidad
    
    # Buscar \b1[Tt]\b
    memoria_1t = re.search(r'\b1[Tt]', texto)
    if memoria_1t:
        return '_1T'
    
    # Buscar \b(128|256|512)\b
    memorias_sin_unidades = re.search(r'\b(128|256|512)\b', texto)
    if memorias_sin_unidades:
        return memorias_sin_unidades.group(0)
    
    return None
    
def es_tienda(texto: str) -> bool:
    if pd.isna(texto):
        return None
    words_to_find = ('reacondicionado', 'tienda')
    for word in words_to_find:
        if word in texto:
            return True 
    return False 

def tiene_garantia(texto: str):
    if pd.isna(texto):
        return None
    words_to_find = ('garantia', 'care', 'factura')
    for word in words_to_find:
        if word in texto:
            return True 
    return False 


# In[7]:


missing_values = df_original.isnull().sum()
print(missing_values)
df['bateria'] = df_original['comentario'].apply(encontrar_bateria)
df['memoria'] = df_original['comentario'].apply(encontrar_memoria)
df['tienda'] = df_original['comentario'].apply(es_tienda)
df['garantia'] = df_original['comentario'].apply(tiene_garantia)

missing_values = df.isnull().sum()
print(missing_values)


# In[8]:


df['tienda'].describe()


# In[9]:


carpeta = "5_data_from_comments"
df.to_csv(carpeta + '/' + nombre_archivo + '.csv')

