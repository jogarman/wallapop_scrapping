# FOR TEST ONLY
from utils.run_wallascrap import run_wallascrap

# 'new', 'as_good_as_new', 'good'
def run_01_scrapper_gopro():
    item_name = 'gopro 9'
    municipio = 'Madrid'
    distancia = '60'
    precio_minimo = '100'
    estado = 'as_good_as_new'
    run_wallascrap(item_name, municipio, estado, distancia, precio_minimo)


######################################
#####        02_join_tables      #####
######################################


run_01_scrapper_gopro()