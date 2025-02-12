#!/usr/bin/env python
# coding: utf-8

# Downloads description of articles
# Cargo un archivo en forma de dataframe, exitraigo un sub-dataframe, scrapeo el comentario de wallapop y lo retorno en un df que es id - descripcion

# In[13]:


import os
import pandas as pd
import re
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import time


# In[14]:


# Selecciono el CSV
elemento_a_buscar = "iphone" # para guardar el archivo   <--------
#iphone = int((elemento_a_buscar).split()[1]) # 12, 14 o 15


# In[ ]:


# Cargo archivo
carpeta = "../data/3_feature_engineering"
fecha = datetime.now().strftime("%Y%m%d")
#fecha = "20250117"
archivo = carpeta + '/' + elemento_a_buscar.split()[0] + '_' + fecha + '.xlsx'
print(archivo)
df_original = pd.read_excel(carpeta + '/' + elemento_a_buscar.split()[0] + '_' + fecha + '.xlsx')
df_original.head()


# In[16]:


# Selecciono el sub-dataframe.
# Selecciono:       as_good_as_new 
#                   iphone 15. 
#                   bateria = NaN
# Son 263 apariciones
# estado = new...
df_to_scrap = df_original[#(df_original['estado'] == estado) & 
                          #(df_original['gen'] == iphone) & 
                          (pd.isna(df_original['bateria']))]
#df_to_scrap = df_original
df_to_scrap.reset_index(drop=True, inplace = True)
df_to_scrap.head(5)


# In[17]:


# Función de scrapeo comentarios
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# no existe https://es.wallapop.com/item/iphone-15-128gb-como-nuevo-1069439182
# si existe https://es.wallapop.com/item/iphone-15-pro-max-esim-256gb-1069441441


# In[18]:


# 263 anuncios - 25 min. con sleep de 1
# 5s por anuncio si va lento. Si va bien 1.5s
# Escrapeo objetos de:
# Vendedor, cuadro datos, cuadro envio, cuadro comentario, cuadro 'editado views y likes'
# por ahora solo comentario


def scrap_comments(df):
    """
    Dado un df con una columna 'url de wallapop':
    accede a la URL, 
    busca el comentario y
    lo guarda en la columna 'comentario'
    """
    df_len = len(df)
    df['comentario'] = None
    if 'url' not in df.columns:
        raise ValueError("Error: La columna 'url' no existe en el DataFrame.")
    print("Tiempo estimado de inicio: 25s...")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get(df.loc[0]['url']) 
    WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "onetrust-reject-all-handler"))).click()  # Quita cookies y carga primera web
    for index in range(len(df)):
        start_time = time.time()  # Marca de tiempo al inicio de la iteración
        print(index, '/', df_len)
        driver.get(df.loc[index]['url']) 
        try:
            elemento_comentario = driver.find_element(By.CSS_SELECTOR, "#__next > main > div > div.item-detail_ItemDetail__container__8p25r.pb-5 > section.justify-content-around.d-flex.py-4 > div.item-detail_ItemDetail__card__jnUEv.pb-5 > div.px-4 > div.item-detail_ItemDetail__separator__SCH3p.py-2 > section").text
            df.loc[index, 'comentario'] = elemento_comentario
            print(df.loc[index]['url'], ': \n', elemento_comentario)
        except:
            #element = driver.find_element(By.CLASS_NAME, "not-found-page_Error__title__Dky_8")
            df.loc[index, 'comentario'] = "not found"
            print(df.loc[index]['url'], df.loc[index, 'comentario'])

        end_time = time.time()  # Marca de tiempo al final de la iteración
        execution_time = end_time - start_time  # Calcula el tiempo de ejecución
        print(f"Estimated time to finish: {((df_len - index) * execution_time/60):.2f}min")
        print(f"{execution_time:.2f}s")  
    driver.quit()
    return df

#file = "1_datos_raw/" + "20250102_gopro 13_as_good_as_new.csv"
#df_test = pd.read_csv(file)
df_with_comments = scrap_comments(df_to_scrap)


# In[19]:


df_with_comments.head(4)


# In[20]:


subdf_comentarios = df_with_comments[['id', 'comentario']]
subdf_comentarios


# In[21]:


# Guardo comentarios finales en el df original
df_original = pd.merge(df_original, subdf_comentarios, on='id', how='left')


# In[22]:


df_original.head(5)


# In[23]:


nombre_archivo_csv = df_original
carpeta = "4_download_description"
nombre_archivo_pkl = fecha + '_' + elemento_a_buscar
df_original.to_csv(carpeta + '/' + nombre_archivo_pkl + '.csv')

