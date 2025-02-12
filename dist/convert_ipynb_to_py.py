import os
import re
import shutil
import filecmp
from utils import convertir_ipynb_en_py, Color as c
import glob

def print_convertido(file):
    print(f"{c.VERDE}Convertido: {file}{c.RESET}")
def print_excluido(file):
    print(f"{c.AZUL_CLARO}Excluido: {file}{c.RESET}")
def print_copiado(file):
    print(f"{c.VERDE_OSCURO}Copiado: {file}{c.RESET}")
def print_ya_existe(file):
    print(f"{c.AZUL_CLARO}Ya existe: {file}{c.RESET}")
def print_actualizado(file):
    print(f"{c.VERDE}Actualizado: {file}{c.RESET}")

def convertir_archivos_ipynb_a_py(carpeta_origen, carpeta_destino, excluyentes):
    if not os.path.exists(carpeta_destino):
        os.makedirs(carpeta_destino)

    for root, dirs, files in os.walk(carpeta_origen):
        for file in files:
            if file.endswith(".ipynb") and file != os.path.basename(__file__):
                ruta_completa = os.path.join(root, file)
                ruta_destino = os.path.join(carpeta_destino, file.replace(".ipynb", ".py"))

                # Verificar si el archivo está en la lista de excluyentes
                excluir = False
                for patron in excluyentes:
                    if re.match(patron, file):
                        excluir = True
                        break

                if not excluir:
                    if os.path.exists(ruta_destino):
                        if filecmp.cmp(ruta_completa, ruta_destino, shallow=False):
                            print_ya_existe(file)
                        else:
                            convertir_ipynb_en_py(ruta_completa)
                            os.remove(ruta_destino)  # Eliminar el archivo de destino si ya existe
                            os.rename(ruta_completa.replace(".ipynb", "_temp.py"), ruta_destino)
                            print_actualizado(file)
                    else:
                        convertir_ipynb_en_py(ruta_completa)
                        os.rename(ruta_completa.replace(".ipynb", "_temp.py"), ruta_destino)
                        print_convertido(file)
                else:
                    print_excluido(file)

    # Copiar archivos .py a la carpeta de destino
    for root, dirs, files in os.walk(carpeta_origen):
        for file in files:
            if file.endswith(".py") and file != os.path.basename(__file__):
                ruta_completa = os.path.join(root, file)
                ruta_destino = os.path.join(carpeta_destino, file)

                # Verificar si el archivo está en la lista de excluyentes
                excluir = False
                for patron in excluyentes:
                    if re.match(patron, file):
                        excluir = True
                        break

                if not excluir:
                    if os.path.exists(ruta_destino):
                        if filecmp.cmp(ruta_completa, ruta_destino, shallow=False):
                            print_ya_existe(file)
                        else:
                            shutil.copy2(ruta_completa, ruta_destino)
                            print_actualizado(file)
                    else:
                        shutil.copy2(ruta_completa, ruta_destino)
                        print_copiado(file)
                else:
                    print_excluido(file)

def eliminar_posibles_archivos_temp(carpeta):
    """
    Elimina todos los archivos llamados *_temp.py o *_temp.ipynb 
    """
    # Buscar archivos que coinciden con *_temp.py y *_temp.ipynb en la carpeta
    archivos_temp = glob.glob(os.path.join(carpeta, '*_temp.py')) + glob.glob(os.path.join(carpeta, '*_temp.ipynb'))
    for archivo in archivos_temp:
        try:
            os.remove(archivo)
            print(f"Archivo eliminado: {archivo}")
        except Exception as e:
            print(f"No se pudo eliminar el archivo {archivo}. Error: {e}")

if __name__ == "__main__":
    carpeta_origen = os.path.dirname(os.path.abspath(__file__))
    carpeta_destino = os.path.join(carpeta_origen, "../build")
    excluyentes = [
        r"^01_.*",  # Excluir archivos que empiezan por 01_
        # Agrega más patrones de exclusión aquí
    ]

    eliminar_posibles_archivos_temp(carpeta_origen)
    convertir_archivos_ipynb_a_py(carpeta_origen, carpeta_destino, excluyentes)
