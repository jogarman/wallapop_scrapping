import os
import subprocess


############################### 
###### xxxxx_scraper.py ####### 
############################### 
def run_wallascrap(item_name, municipio, estado, distancia, precio_minimo, env=None):
    print("def run_wallascrap...")
    python_executable = os.path.join('..', '.env', 'Scripts', 'python.exe')
    if not os.path.exists(python_executable):
        print(f"Error: El ejecutable de Python no se encuentra en {python_executable}")
        return
    command = [
        python_executable, '01_wallascrap.py',
        '--item_name', item_name,
        '--municipio', municipio,
        '--estado', estado,
        '--distancia', str(distancia),
        '--precio_minimo', str(precio_minimo)
    ]
    print("command: ", command)
    result = subprocess.run(command, capture_output=True, text=True, env=env)
    print("stdout: ", result.stdout)
    if result.stderr:
        print("stderr: ", result.stderr)