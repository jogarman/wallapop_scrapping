import nbformat
import os
from nbconvert import PythonExporter

def convertir_ipynb_en_py(nombre_jupiter, first_bit = 1):
    temp_file = nombre_jupiter.replace(".ipynb", "_temp.py")
    if not os.path.exists(temp_file):
        try:
            with open(nombre_jupiter, encoding='utf-8') as f:
                notebook = nbformat.read(f, as_version=4)

            python_exporter = PythonExporter()
            python_script, _ = python_exporter.from_notebook_node(notebook)
            with open(temp_file, "w", encoding='utf-8') as f:
                f.write(python_script)
            print(f"{temp_file} ha sido creado.")
        except Exception as e:
            if first_bit == 1:
                print(f"Error al convertir {nombre_jupiter}")
                print("Reintentando...")
                convertir_ipynb_en_py(nombre_jupiter, first_bit = 0) # intenta de nuevo si falla
            print(f"Error al convertir {nombre_jupiter}: {e}")
    else:
        print(f"{temp_file} no se crea porque ya existe.")