#!/usr/bin/env python
# coding: utf-8

# ## Featuring engineering
# creo variables como, si tiene color, si tiene emojis, si pone "vendo", si pone "revisado"

# In[11]:


import os
import pandas as pd
import re
from datetime import datetime


# In[12]:


carpeta = "../2_datos_por_fecha"
fecha = datetime.now().strftime("%Y%m%d")
#fecha = "20250117"


# In[13]:


df = pd.read_csv(carpeta + '/' + "iphone_" + fecha + '.csv', index_col=0)


# In[14]:


df


# In[15]:


# Asigno columnas MODELO, MEMORIA, COLOR, BATERIA....

# Creo una columna en la que pongo que iphone es (14, 15 o 16..) y que tipo. 
# Gen
# Model
for index in range(len(df)):
    df['gen'] = 'vacio'
    df['modelo'] = 'modelo'

def asignar_gen(nombre):
    if '14' in nombre:
        return '14'
    elif '15' in nombre:
        return '15'
    elif '16' in nombre:
        return '16'
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

# Función para asignar el valor de la columna "bateria"
def asignar_bateria(nombre):
    # Buscar números entre 80 y 100 en el nombre
    bateria = re.findall(r'\b([8-9][0-9]|100)\b', nombre)
    if bateria:
        return int(bateria[0])  # Retorna el primer número que encuentra
    return "n/a"

# Aplicar las funciones al DataFrame
df['gen'] = df['nombre'].apply(asignar_gen)
df['mod'] = df['nombre'].apply(asignar_modelo)
df['memoria'] = df['nombre'].apply(asignar_memoria)
df['bateria'] = df['nombre'].apply(asignar_bateria)
orden_columnas = ['id','fecha', 'gen', 'mod', 'memoria', 'bateria','precio', 'estado', 'nombre', 'scrap_locat' , 'dist_scrap_locat',
    'reservado', 'url']
df = df[orden_columnas]
df


# In[16]:


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

df['tiene_color'] = df['nombre'].apply(tiene_color)
df['tiene_emojis'] = df['nombre'].apply(tiene_emojis)
df['tiene_revisado'] = df['nombre'].apply(tiene_revisado)
df


# In[17]:


carpeta = "3_feature_engineering"
if not os.path.exists(carpeta):
    os.makedirs(carpeta)
nombre_archivo = f"{carpeta}/iphone_{fecha}.xlsx" # excel ofrece ventajas para abrirlo en tableu. Pero no recuerdo cuales
df = df.reset_index(drop=True) # sin indice
df.to_excel(nombre_archivo, index=False)
#print(nombre_archivo_csv, "creado exitosamente")


# In[ ]:




