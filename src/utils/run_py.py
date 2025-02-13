import subprocess

def run_py(temp_file):
    print("ejecutando: ", "python", temp_file)
    subprocess.run(["python", temp_file])
    print(f"{temp_file} ejecutado.")