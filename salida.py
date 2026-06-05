import json
from lexico import analizar_lexico

def generar_salida(texto):
    tokens = analizar_lexico(texto)

    valores = {}
    indices_numero = [i for i, (t, v) in enumerate(tokens) if t == 'NUMERO']

    if len(indices_numero) >= 1:
        valores['mesa'] = int(tokens[indices_numero[0]][1])
    if len(indices_numero) >= 2:
        valores['cantidad'] = int(tokens[indices_numero[1]][1])

    for tipo, valor in tokens:
        if tipo == 'PLATO':
            valores['plato'] = valor
        if tipo == 'MODIFICADOR':
            valores['modificador'] = valor

    #JSON file
    salida = {
        "mesa": valores.get('mesa'),
        "cantidad": valores.get('cantidad'),
        "plato": valores.get('plato'),
        "modificador": valores.get('modificador', 'NINGUNO'),
        "estado": "ACEPTADO"
    }

    return salida