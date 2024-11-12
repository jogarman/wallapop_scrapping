def existe_cadena(str_1, cadenas_buscadas, cadenas_excluyentes):
    nombre_list = str_1.split()
    nombre_list = set(nombre_list)
    if nombre_list.intersection(cadenas_buscadas):
        if not nombre_list.intersection(cadenas_excluyentes):
            return True
        else:
            return False
    else:
        return False

def ya_existe_articulo(id, df):
    existe = df['id'].isin([id]).any()
    return existe