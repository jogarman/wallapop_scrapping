import re

def existe_cadena(name, cadenas_buscadas, cadenas_excluyentes):
    nombre_list = name.split()
    nombre_list = set(nombre_list)
    if nombre_list.intersection(cadenas_buscadas):
        if not nombre_list.intersection(cadenas_excluyentes):
            return True
        else:
            return False
    else:
        return False

"""
Primero mira que la primera palabra sea la buscada. Para un iphone casi todos empiezan por iphone o movil.
    Si así es mira que sea el modelo, en este caso busca que ponga "iphone 16" y "phone 1 6" que por algun motivo 
    algunos usuarios ponen espacios

Si no aplica la función anterior, mucho más restrictiva. 
xx en mi caso es 16
"""
def is_iphone_xx(name, xx, cadenas_buscadas, cadenas_excluyentes):
    name_splited = name.split(" ")
    if (name_splited[0] in ("movil", "móvil", "iphone", "smartphone")): # si empieza por "movil" o similar es mucho menos restrictivo.
        if ((xx in name_splited) and ('4' not in name_splited) and ('5' not in name_splited)): # para evitar que casos como 'iphone 4 16 gb azul'
            return True
        else:
            
            return False
    else:
        return existe_cadena(name, cadenas_buscadas, cadenas_excluyentes) # llama a ua funcion mas restrictiva


def ya_existe_articulo(id, df):
    existe = df['id'].isin([id]).any()
    return existe

def item_reservado(elem):
    try:
        elemento_reservado = elem.find_element(By.CSS_SELECTOR, ".clase_indicativa_de_reservado")
        return True
    except:
        return False