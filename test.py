import time

for minuto in range(10):
    nombre_archivo = f"{minuto}.txt"
    with open(nombre_archivo, "w") as archivo:
        pass  # Crea el archivo vacío.
    print(f"Archivo {nombre_archivo} creado.")
    time.sleep(60)  # Espera 60 segundos antes de la siguiente iteración.