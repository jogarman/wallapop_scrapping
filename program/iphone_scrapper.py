# Este código solo ejecuta reiteradas veces 01_wallascrap.py con los distintos parametros 
# para IPHONE 14 15 y 16
import sys
import subprocess
import os

def run_wallascrap(item_name, municipio, estado, distancia, precio_minimo):
    print("def run_wallascrap...")
    python_executable = os.path.join('.env', 'Scripts', 'python.exe')
    command = [
        python_executable, '01_wallascrap.py',
        '--item_name', item_name,
        '--municipio', municipio,
        '--estado', estado,
        '--distancia', str(distancia),
        '--precio_minimo', str(precio_minimo)
    ]
    print("command: ", command)
    result = subprocess.run(command, capture_output=True, text=True)
    # Mostrar la salida en el widget de texto
    print(result.stdout)
    if result.stderr:
        print(result.stderr)


# 'new', 'as_good_as_new', 'good'

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