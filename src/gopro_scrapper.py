# Scrapea las gopros 10, 11 y 12
# NO FUNCIONA BIEN
# Este código solo ejecuta reiteradas veces 01_wallascrap.py con los distintos parametros 
# para gopro 10, 11 y 12
# luego hace las transformaciones necesarias

from utils.run_py import run_py
from utils.run_wallascrap import run_wallascrap

#############################################
##### 01_wallascrap gopros 10, 11 y 12 ######
#############################################

# 'new', 'as_good_as_new', 'good'
def run_01_scrapper_gopro():
    item_name = 'gopro 10'
    municipio = 'Madrid'
    estado = 'new'
    distancia = '60'
    precio_minimo = '100'
    run_wallascrap(item_name, municipio, estado, distancia, precio_minimo)
    estado = 'as_good_as_new'
    run_wallascrap(item_name, municipio, estado, distancia, precio_minimo)
    estado = 'good'
    run_wallascrap(item_name, municipio, estado, distancia, precio_minimo)

    item_name = 'gopro 11'
    municipio = 'Madrid'
    estado = 'new'
    distancia = '60'
    precio_minimo = '110'
    run_wallascrap(item_name, municipio, estado, distancia, precio_minimo)
    estado = 'as_good_as_new'
    run_wallascrap(item_name, municipio, estado, distancia, precio_minimo)
    estado = 'good'
    run_wallascrap(item_name, municipio, estado, distancia, precio_minimo)

    item_name = 'gopro 12'
    municipio = 'Madrid'
    estado = 'new'
    distancia = '60'
    precio_minimo = '120'
    run_wallascrap(item_name, municipio, estado, distancia, precio_minimo)
    estado = 'as_good_as_new'
    run_wallascrap(item_name, municipio, estado, distancia, precio_minimo)
    estado = 'good'
    run_wallascrap(item_name, municipio, estado, distancia, precio_minimo)

    item_name = 'gopro 13'
    municipio = 'Madrid'
    estado = 'new'
    distancia = '60'
    precio_minimo = '130'
    run_wallascrap(item_name, municipio, estado, distancia, precio_minimo)
    estado = 'as_good_as_new'
    run_wallascrap(item_name, municipio, estado, distancia, precio_minimo)
    estado = 'good'
    run_wallascrap(item_name, municipio, estado, distancia, precio_minimo)

######################################
#####        02_join_tables      #####
######################################

run_01_scrapper_gopro()
run_py("02_join_tables_gopro.py")
run_py("03_feature_engineering_gopro.py")

