import os
import re
from utils import convertir_ipynb_en_py

def convertir_archivos_ipynb_a_py(carpeta_origen, excluyentes):
    for root, dirs, files in os.walk(carpeta_origen):
        for file in files:
            if file.endswith(".ipynb") and file != os.path.basename(__file__):
                ruta_completa = os.path.join(root, file)
                ruta_destino = os.path.join(root, file.replace(".ipynb", ".py"))

                # Verificar si el archivo está en la lista de excluyentes
                excluir = False
                for patron in excluyentes:
                    if re.match(patron, file):
                        excluir = True
                        break

                if not excluir:
                    convertir_ipynb_en_py(ruta_completa)
                    os.rename(ruta_completa.replace(".ipynb", "_temp.py"), ruta_destino)
                    print(f"Convertido: {ruta_completa} -> {ruta_destino}")
                else:
                    print(f"Excluido: {ruta_completa}")

if __name__ == "__main__":
    carpeta_origen = os.path.dirname(os.path.abspath(__file__))
    excluyentes = [
        r"^01_.*",  # Excluir archivos que empiezan por 01_
        # Agrega más patrones de exclusión aquí
    ]

    convertir_archivos_ipynb_a_py(carpeta_origen, excluyentes)
