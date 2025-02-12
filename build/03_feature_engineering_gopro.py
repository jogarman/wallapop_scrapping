#!/usr/bin/env python
# coding: utf-8

# ## Featuring engineering
# obtengo variables como el modelo de la gopro

# In[1]:


import os
import pandas as pd
import re
from datetime import datetime


# In[ ]:


carpeta = "../data/2_datos_por_fecha"
fecha = datetime.now().strftime("%Y%m%d")
#fecha = "20250102"


# In[3]:


df = pd.read_csv(carpeta + '/' + "gopro_" + fecha + '.csv', index_col=0)


# In[4]:


df


# In[5]:


# Asigno columnas MODELO, MEMORIA, COLOR, BATERIA....

# Creo una columna en la que pongo que iphone es (14, 15 o 16..) y que tipo. 
# Gen
# Model
for index in range(len(df)):
    df['gen'] = 'vacio'
    df['modelo'] = 'modelo'

def asignar_gen(nombre):
    if '8' in nombre:
        return '8'
    elif '9' in nombre:
        return '9'
    elif '10' in nombre:
        return '10'
    elif '11' in nombre:
        return '11'
    elif '12' in nombre:
        return '12'
    elif '13' in nombre:
        return '13'
    elif '14' in nombre:
        return '14'
    return "n/a"

# Función para asignar el valor de la columna "modelo"
def asignar_modelo(nombre):
    if 'pro max' in nombre.lower():
        return 'pro max'
    elif 'pro' in nombre.lower():
        return 'pro'
    elif 'plus' in nombre.lower():
        return 'plus'
    else:
        return 'basic'

def asignar_memoria(nombre):
    if '128' in nombre.lower():
        return '128'
    elif '256' in nombre.lower():
        return '256'
    elif '512' in nombre.lower():
        return '512'
    elif '1tb' in nombre.lower():
        return '1tb'
    else:
        return 'n/a'
colores_iphones = ["Púrpura", "Verde", "Blanco", "Azul", "Negro", "Rojo", "Grafito", "Plata", "Oro", "Morado", "titanio", "Ultramarino", 'rojo', 'azul', 'negro', 'blanco', 'verde', 'amarillo', 'rosado', 'rosa', 'gris', 'morado', 'naranja']
# Imprimir todos los colores
def tiene_color(nombre):
    return any(color in nombre.lower() for color in colores_iphones)
def tiene_emojis(nombre):
    return bool(re.search(r'[^\w\s,]', nombre))  # Busca caracteres no alfanuméricos que son emojis
def tiene_vendo(nombre):
    return 'vendo' in nombre.lower()
def tiene_revisado(nombre):
    return 'revisado' in nombre.lower()
    
# Función para asignar el valor de la columna "bateria"
def asignar_bateria(nombre):
    # Buscar números entre 80 y 100 en el nombre
    bateria = re.findall(r'\b([8-9][0-9]|100)\b', nombre)
    if bateria:
        return int(bateria[0])  # Retorna el primer número que encuentra
    return "n/a"

# Aplicar las funciones al DataFrame
df['gen'] = df['nombre'].apply(asignar_gen)
# df['mod'] = df['nombre'].apply(asignar_modelo)
# df['memoria'] = df['nombre'].apply(asignar_memoria)
# df['bateria'] = df['nombre'].apply(asignar_bateria)
orden_columnas = ['id','fecha', 'gen', 'precio', 'estado', 'nombre', 'scrap_locat' , 'dist_scrap_locat',
    'reservado', 'url']
df = df[orden_columnas]
df


# In[6]:


# df['tiene_color'] = df['nombre'].apply(tiene_color)
# df['tiene_emojis'] = df['nombre'].apply(tiene_emojis)
# df['tiene_revisado'] = df['nombre'].apply(tiene_revisado)


# In[7]:


carpeta = "../3_feature_engineering"
if not os.path.exists(carpeta):
    os.makedirs(carpeta)
nombre_archivo = f"{carpeta}/gopro_{fecha}.xlsx" # excel ofrece ventajas para abrirlo en tableu. Pero no recuerdo cuales
df = df.reset_index(drop=True) # sin indice
df.to_excel(nombre_archivo, index=False)
print(nombre_archivo, "creado exitosamente")


# In[ ]:




