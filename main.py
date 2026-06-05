from sintactico import analizar_sintactico
from semantico import analizar_semantico
from salida import generar_salida
import json

def compilar_comanda(texto):
    print(f"\n{'='*50}")
    print(f"COMANDA: {texto}")
    print('='*50)

    #sintactico
    valido, mensaje_sint = analizar_sintactico(texto)
    print(f"[SINTÁCTICO] {mensaje_sint}")
    if not valido:
        print(">> Comanda RECHAZADA.\n")
        return

    #semantico
    valido, mensajes_sem = analizar_semantico(texto)
    for m in mensajes_sem:
        print(f"[SEMÁNTICO]  {m}")
    if not valido:
        print(">> Comanda RECHAZADA.\n")
        return

    #salida
    resultado = generar_salida(texto)
    print(f"[SALIDA]     {json.dumps(resultado)}")
    print(">> Comanda ACEPTADA.\n")
    
    #python app.py