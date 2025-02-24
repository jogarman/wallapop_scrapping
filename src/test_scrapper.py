# FOR TEST ONLY
from utils.run_wallascrap import run_wallascrap
from utils.process_and_run_jupiter import process_and_run_jupiter
#from utils.upload_files_and_folders_to_s3 import upload_files_and_folders_to_s3
from utils.get_if_same_csv_exists import *


# 'new', 'as_good_as_new', 'good'
def run_01_test():
    item_name = 'iphone 15'
    municipio = 'Madrid'
    estado = 'new'
    distancia = '60'
    precio_minimo = '100'
    run_wallascrap(item_name, municipio, estado, distancia, precio_minimo)
    estado = 'as_good_as_new'
    run_wallascrap(item_name, municipio, estado, distancia, precio_minimo)

    item_name = 'iphone 15'
    municipio = 'Madrid'
    estado = 'new'
    distancia = '60'
    precio_minimo = '100'
    run_wallascrap(item_name, municipio, estado, distancia, precio_minimo)
    estado = 'as_good_as_new'
    run_wallascrap(item_name, municipio, estado, distancia, precio_minimo)

    item_name = 'gopro 13'
    municipio = 'Madrid'
    estado = 'new'
    distancia = '60'
    precio_minimo = '100'
    run_wallascrap(item_name, municipio, estado, distancia, precio_minimo)
    estado = 'as_good_as_new'
    run_wallascrap(item_name, municipio, estado, distancia, precio_minimo)

    item_name = 'gopro 13'
    municipio = 'Madrid'
    estado = 'new'
    distancia = '60'
    precio_minimo = '100'
    run_wallascrap(item_name, municipio, estado, distancia, precio_minimo)
    estado = 'as_good_as_new'
    run_wallascrap(item_name, municipio, estado, distancia, precio_minimo)

######################################
#####        02_join_tables      #####
######################################

run_01_test()
process_and_run_jupiter('02_join_tables_iphone.ipynb')
process_and_run_jupiter('03_feature_engineering_iphone.ipynb')
process_and_run_jupiter('02_join_tables_gopro.ipynb')
process_and_run_jupiter('03_feature_engineering_gopro.ipynb')

######################################
#####        Copy to s3          #####
######################################

#upload_files_and_folders_to_s3()