#!/usr/bin/env python
# coding: utf-8

# ## Junta tablas de gopro

# In[11]:


import os
import pandas as pd
import re
from datetime import datetime
import nbformat
from nbconvert import PythonExporter
import subprocess


# In[12]:


# SELECCIONAR QUÉ PRODUCTO QUEREMOS AGRUPAR # solo cambia este chunk
producto = "gopro"
fecha = datetime.now().strftime("%Y%m%d")
#fecha = '20250117'  # Fecha en formato yyyymmdd


# In[13]:


def read_and_join_csvs_by_date(fecha, producto, folder_path='../1_datos_raw'):
    """
    Función que toma una fecha en formato 'yyyymmdd' y busca los archivos CSV 
    en el folder_path que comiencen con esa fecha, añadiendo la fecha como columna
    y realizando un outer join entre ellos.

    Args:
    -(fecha) (str): Fecha en formato 'yyyymmdd'.
    - folder_path (str): Directorio donde se encuentran los archivos CSV. Por defecto, es el directorio actual.

    Returns:
    - pd.DataFrame: DataFrame resultante del outer join entre los CSV encontrados con la misma fecha,
                    incluyendo una columna "fecha".
    """
    # Listar todos los archivos en la carpeta
    files = os.listdir(folder_path)
    
    # Filtrar los archivos que comienzan con la fecha proporcionada
    csv_files = []
    for f in files:
        if f.startswith(fecha) and f.endswith('.csv'):
            csv_files.append(f)
    product_files = []
    for f in csv_files:
        if producto in f.lower():
            product_files.append(f)

    print(product_files)
    # Verificar que haya más de un archivo para realizar el join
    if len(product_files) > 1:
        # Leer los archivos con la misma fecha y añadir la columna "fecha"
        dfs = []
        for f in product_files:
            df = pd.read_csv(os.path.join(folder_path, f))
            df['fecha'] =(fecha)  # Añadir la columna con la fecha
            dfs.append(df)

        # Hacer un join de todos los DataFrames de esa fecha usando outer join
        merged_df = dfs[0]
        for df in dfs[1:]:
            merged_df = merged_df.merge(df, how='outer')  # Outer join para añadir registros no coincidentes
        
        return merged_df
    else:
        print(f"No se encontraron suficientes archivos con la fecha {fecha} para hacer un join.")
        return None

df = read_and_join_csvs_by_date(fecha, producto)

## Para arreglar los actuales
df['scrap_locat'] = 'madrid'
df['dist_scrap_locat'] = 60
column_order = df.columns.tolist()
column_order.insert(5, column_order.pop(column_order.index('scrap_locat')))
column_order.insert(6, column_order.pop(column_order.index('dist_scrap_locat')))
df = df[column_order]
########

del df['Unnamed: 0']
df


# In[14]:


if producto == "iphone":
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


# In[ ]:


carpeta = "../data/2_datos_por_fecha"
nombre_archivo_pkl = carpeta + '/' + producto + '_' + fecha + '.csv'
df.to_csv(nombre_archivo_pkl)
print(nombre_archivo_pkl)

