# Scrapea las gopros 10, 11 y 12
# NO FUNCIONA BIEN
# Este código solo ejecuta reiteradas veces 01_wallascrap.py con los distintos parametros 
# para gopro 10, 11 y 12
# luego hace las transformaciones necesarias

import subprocess
from utils import convertir_ipynb_en_py, ejecutar_py, run_wallascrap, borrar_temp

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

def run(program_ipynb_ini):
    program_ipynb_temp = program_ipynb_ini.replace(".ipynb", "_temp.py")
    convertir_ipynb_en_py(program_ipynb_ini)
    ejecutar_py(program_ipynb_temp)
    borrar_temp(program_ipynb_temp)


run_01_scrapper_gopro()
run("02_join_tables_gopro.ipynb")
run("03_feature_engineering_gopro.ipynb")
