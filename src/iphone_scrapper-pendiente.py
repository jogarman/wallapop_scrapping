# Este código solo ejecuta reiteradas veces 01_wallascrap.py con los distintos parametros 
# para IPHONE 14 15 y 16

from utils.run_py import run_py
from utils.run_wallascrap import run_wallascrap

# 'new', 'as_good_as_new', 'good'
def run_01_scrapper_iphone():
    item_name = 'iphone 14'
    municipio = 'Madrid'
    estado = 'new'
    distancia = '60'
    precio_minimo = '250'
    run_wallascrap(item_name, municipio, estado, distancia, precio_minimo)
    estado = 'as_good_as_new'
    run_wallascrap(item_name, municipio, estado, distancia, precio_minimo)
    estado = 'good'
    run_wallascrap(item_name, municipio, estado, distancia, precio_minimo)

    item_name = 'iphone 15'
    municipio = 'Madrid'
    estado = 'new'
    distancia = '60'
    precio_minimo = '300'
    run_wallascrap(item_name, municipio, estado, distancia, precio_minimo)
    estado = 'as_good_as_new'
    run_wallascrap(item_name, municipio, estado, distancia, precio_minimo)
    estado = 'good'
    run_wallascrap(item_name, municipio, estado, distancia, precio_minimo)

    item_name = 'iphone 16'
    municipio = 'Madrid'
    estado = 'new'
    distancia = '60'
    precio_minimo = '300'
    run_wallascrap(item_name, municipio, estado, distancia, precio_minimo)
    estado = 'as_good_as_new'
    run_wallascrap(item_name, municipio, estado, distancia, precio_minimo)
    estado = 'good'
    run_wallascrap(item_name, municipio, estado, distancia, precio_minimo)

######################################
#####        02_join_tables      #####
######################################


run_01_scrapper_iphone()
run_py("02_join_tables_iphone.py")
run_py("03_feature_engineering_iphone.py")
run_py("04_download_description.py")
run_py("04_download_description.py")
run_py("05_get_data_from_comments.py") 