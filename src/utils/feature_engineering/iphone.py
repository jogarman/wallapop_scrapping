import re

def asignar_gen(nombre):
    if '14' in nombre:
        return '14'
    elif '15' in nombre:
        return '15'
    elif '16' in nombre:
        return '16'
    return "n/a"

# Función para asignar el valor de la columna "modelo"
def asignar_modelo(nombre):
    if 'pro max' in nombre.lower():
        return 'pro max'
    elif 'pro' in nombre.lower():
        return 'pro'
    elif 'plus' in nombre.lower():
        return 'plus'
    else:
        return 'basic'

def asignar_memoria(nombre):
    if '128' in nombre.lower():
        return '128'
    elif '256' in nombre.lower():
        return '256'
    elif '512' in nombre.lower():
        return '512'
    elif '1tb' in nombre.lower():
        return '1tb'
    else:
        return 'n/a'

# Función para asignar el valor de la columna "bateria"
def asignar_bateria(nombre):
    # Buscar números entre 80 y 100 en el nombre
    bateria = re.findall(r'\b([8-9][0-9]|100)\b', nombre)
    if bateria:
        return int(bateria[0])  # Retorna el primer número que encuentra
    return "n/a"

# Imprimir todos los colores
colores_iphones = ["Púrpura", "Verde", "Blanco", "Azul", "Negro", "Rojo", "Grafito", "Plata", "Oro", "Morado", "titanio", "Ultramarino", 'rojo', 'azul', 'negro', 'blanco', 'verde', 'amarillo', 'rosado', 'rosa', 'gris', 'morado', 'naranja']

def tiene_color(nombre):
    return any(color in nombre.lower() for color in colores_iphones)
def tiene_emojis(nombre):
    return bool(re.search(r'[^\w\s,]', nombre))  # Busca caracteres no alfanuméricos que son emojis
def tiene_vendo(nombre):
    return 'vendo' in nombre.lower()
def tiene_revisado(nombre):
    return 'revisado' in nombre.lower()