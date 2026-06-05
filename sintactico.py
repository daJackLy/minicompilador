from lexico import analizar_lexico

#la estructura valida es:
#MESA NUMERO PEDIR NUMERO PLATO (MODIFICADOR es opcional)

def analizar_sintactico(texto):
    tokens = analizar_lexico(texto)
    tipos = [tipo for tipo, valor in tokens]

    estructura_minima = ['MESA', 'NUMERO', 'PEDIR', 'NUMERO', 'PLATO']

    #al menos los 5 tokens
    if len(tipos) < 5:
        return False, "ERROR: La comanda está incompleta."

    #verificar tokens correcton
    if tipos[:5] != estructura_minima:
        return False, f"ERROR: Estructura incorrecta. Se esperaba: MESA NUMERO PEDIR NUMERO PLATO"

    #si hay mas de 5 tokens, el 6to es modificador
    if len(tipos) == 6 and tipos[5] != 'MODIFICADOR':
        return False, "ERROR: El 6to elemento debe ser un modificador válido."

    #si hay tokens deconocidos
    if 'DESCONOCIDO' in tipos:
        return False, "ERROR: Hay palabras no reconocidas en la comanda."

    return True, "OK: Estructura sintáctica correcta."