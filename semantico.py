from lexico import analizar_lexico

INCOMPATIBLES = {
    #postres
    'ARROZ_CON_LECHE': [
        'SIN_SAL',
        'EXTRA_PICANTE',
        'SIN_CEBOLLA',
        'EXTRA_CAMARONES',
        'SIN_LIMON'
    ],

    'MAZAMORRA_MORADA': [
        'EXTRA_PICANTE',
        'SIN_CEBOLLA',
        'EXTRA_CAMARONES'
    ],

    'SUSPIRO_A_LA_LIMENA': [
        'EXTRA_PICANTE',
        'SIN_CEBOLLA',
        'EXTRA_CARNE',
        'EXTRA_POLLO'
    ],

    'PICARONES': [
        'SIN_CEBOLLA',
        'EXTRA_PICANTE',
        'EXTRA_CAMARONES'
    ],

    #seafood
    'CEVICHE': [
        'BIEN_COCIDO',
        'TERMINO_MEDIO',
        'SIN_LIMON'
    ],

    'LECHE_DE_TIGRE': [
        'BIEN_COCIDO',
        'TERMINO_MEDIO',
        'SIN_LIMON'
    ],

    'PARIHUELA': [
        'TERMINO_MEDIO',
        'BIEN_COCIDO',
        'SIN_MARISCOS'
    ],

    'PESCADO_A_LO_MACHO': [
        'SIN_MARISCOS',
        'TERMINO_MEDIO'
    ],

    #carnes
    'LOMO_SALTADO': [
        'TERMINO_MEDIO',  # suponiendo que siempre sale cocido
        'SIN_CEBOLLA'
    ],

    'ANTICUCHOS': [
        'SIN_CARNE',
        'EXTRA_CAMARONES'
    ],

    'SECO_DE_RES': [
        'SIN_CARNE'
    ],

    'CABRITO_A_LA_NORTENA': [
        'SIN_CARNE'
    ],

    #pollo
    'POLLO_A_LA_BRASA': [
        'SIN_POLLO',
        'TERMINO_MEDIO'
    ],

    'AJI_DE_GALLINA': [
        'SIN_POLLO'
    ],

    'CALDO_DE_GALLINA': [
        'SIN_POLLO'
    ],

    #arroces
    'ARROZ_CON_POLLO': [
        'SIN_ARROZ',
        'SIN_POLLO'
    ],

    'ARROZ_CHAUFA': [
        'SIN_ARROZ'
    ],

    'AEROPUERTO': [
        'SIN_ARROZ'
    ],

    #otros
    'PAPA_A_LA_HUANCAINA': [
        'SIN_PAPAS'
    ],

    'CAUSA_RELLENA': [
        'SIN_PAPAS'
    ],

    'TACU_TACU': [
        'SIN_ARROZ'
    ]
}

#rango de cantidades
CANTIDAD_MINIMA = 1
CANTIDAD_MAXIMA = 15

def analizar_semantico(texto):
    tokens = analizar_lexico(texto)
    errores = []

    valores = {tipo: valor for tipo, valor in tokens}
    lista_tipos = [tipo for tipo, valor in tokens]

    #error: cantidad fuera de rango
    indices_numero = [i for i, (t, v) in enumerate(tokens) if t == 'NUMERO']
    if len(indices_numero) >= 2:
        cantidad = int(tokens[indices_numero[1]][1])  # segundo NUMERO = cantidad de platos
        if cantidad < CANTIDAD_MINIMA or cantidad > CANTIDAD_MAXIMA:
            errores.append(f"ERROR: Cantidad '{cantidad}' fuera de rango (1-15).")

    #error: modificador incompatible
    plato = valores.get('PLATO')
    modificador = valores.get('MODIFICADOR')

    if plato and modificador:
        if plato in INCOMPATIBLES and modificador in INCOMPATIBLES[plato]:
            errores.append(f"ERROR: '{modificador}' es incompatible con '{plato}'.")

    #error: numero de mesa invalido
    if len(indices_numero) >= 1:
        mesa = int(tokens[indices_numero[0]][1])  # primer NUMERO = mesa
        if mesa <= 0:
            errores.append(f"ERROR: Número de mesa '{mesa}' no válido.")

    if errores:
        return False, errores
    return True, ["OK: Validación semántica correcta."]