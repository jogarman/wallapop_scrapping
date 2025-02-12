# Este código solo ejecuta reiteradas veces 01_wallascrap.py con los distintos parametros 
# para IPHONE 14 15 y 16

#pendiente
from utils.utils import convertir_ipynb_en_py, ejecutar_py, run_wallascrap, borrar_temp

# 'new', 'as_good_as_new', 'good'
def run_01_scrapper():
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


def run(program_ipynb_ini):
    print("running: ", program_ipynb_ini)
    program_ipynb_temp = program_ipynb_ini.replace(".ipynb", "_temp.py")
    convertir_ipynb_en_py(program_ipynb_ini)
    ejecutar_py(program_ipynb_temp)
    borrar_temp(program_ipynb_temp)

#pendiente de poner como en gopro
run_01_scrapper()
run("02_join_tables_iphone.ipynb")
run("03_feature_engineering_iphone.ipynb")
run("04_download_description.ipynb")
run("04_download_description.ipynb")
run("05_get_data_from_comments.ipynb") 