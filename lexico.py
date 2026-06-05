import re

#TOKENS!!!
TOKENS = [
    ('MESA', r'MESA'),
    ('PEDIR', r'PEDIR'),
    ('NUMERO', r'\d+'),

    ('PLATO',
        r'LOMO_SALTADO|POLLO_A_LA_BRASA|ARROZ_CON_LECHE|CEVICHE|'
        r'TALLARINES|ARROZ_CON_POLLO|SECO_DE_RES|CHICHARRON|'
        r'CAUSA_RELLENA|AJI_DE_GALLINA|PAPA_A_LA_HUANCAINA|'
        r'ANTICUCHOS|TACU_TACU|LECHE_DE_TIGRE|JUANE|'
        r'ROCOTO_RELLENO|CHUPE_DE_CAMARONES|CARAPULCRA|'
        r'ESCABECHE_DE_POLLO|PICARONES|MAZAMORRA_MORADA|'
        r'SUSPIRO_A_LA_LIMENA|TAMAL|CALDO_DE_GALLINA|'
        r'PARIHUELA|ARROZ_CHAUFA|AEROPUERTO|'
        r'PACHAMANCA|CABRITO_A_LA_NORTENA|'
        r'SECO_DE_CABRITO|PESCADO_A_LO_MACHO'
    ),

    ('MODIFICADOR',
        r'SIN_SAL|EXTRA_PICANTE|SIN_CEBOLLA|'
        r'TERMINO_MEDIO|BIEN_COCIDO|SIN_PICANTE|'
        r'EXTRA_PORCION|SIN_PAPAS|CON_ARROZ|SIN_LIMON|'
        r'EXTRA_LIMON|SIN_AJI|EXTRA_SALSA|'
        r'SIN_HUEVO|EXTRA_HUEVO|SIN_ARROZ|'
        r'EXTRA_PAPAS|CON_YUCA|SIN_YUCA|'
        r'EXTRA_POLLO|EXTRA_CARNE|SIN_LECHE|'
        r'SIN_AZUCAR|EXTRA_DULCE|'
        r'PORCION_FAMILIAR|PORCION_PERSONAL|'
        r'EXTRA_CAMARONES|SIN_MARISCOS'
    ),

    ('DESCONOCIDO', r'\S+'),
]

def analizar_lexico(texto):
    tokens_encontrados = []
    texto = texto.strip().upper()

    while texto:
        texto = texto.lstrip()
        match = None

        for tipo, patron in TOKENS:
            regex = re.compile(patron)
            match = regex.match(texto)
            if match:
                valor = match.group(0)
                tokens_encontrados.append((tipo, valor))
                texto = texto[len(valor):]
                break

        if not match:
            break

    return tokens_encontrados