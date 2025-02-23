# FOR TEST ONLY
from utils.run_wallascrap import run_wallascrap
from utils.process_and_run_jupiter import process_and_run_jupiter
from utils.upload_files_and_folders_to_s3 import upload_files_and_folders_to_s3

# 'new', 'as_good_as_new', 'good'
def run_01_scrapper_gopro():
    item_name = 'gopro 10'
    municipio = 'Madrid'
    distancia = '60'
    precio_minimo = '100'
    estado = 'new'
    run_wallascrap(item_name, municipio, estado, distancia, precio_minimo)


######################################
#####        02_join_tables      #####
######################################

run_01_scrapper_gopro()


######################################
#####        Copy to s3          #####
######################################

upload_files_and_folders_to_s3()