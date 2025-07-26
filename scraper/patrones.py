# Archivo con los 26 patrones y predicciones para Baccarat

# Diccionario de patrones: clave = número de patrón, valor = lista de colores
# Los patrones duplicados tienen lista vacía [] para evitar doble detección
PATRONES = {
    1: ['rojo', 'rojo', 'rojo', 'rojo', 'rojo', 'rojo'],
    2: ['azul', 'azul', 'azul', 'azul', 'azul', 'azul'],
    3: ['rojo', 'azul', 'rojo', 'azul', 'rojo', 'azul'],
    4: ['azul', 'rojo', 'azul', 'rojo', 'azul', 'rojo'],
    5: ['rojo', 'rojo', 'azul', 'azul', 'rojo', 'rojo'],
    6: ['rojo', 'azul', 'azul', 'azul', 'rojo', 'rojo'],
    7: ['rojo', 'rojo', 'azul', 'azul', 'azul', 'rojo'],
    8: ['azul', 'azul', 'rojo', 'rojo', 'azul', 'azul'],
    9: ['rojo', 'rojo', 'rojo', 'azul', 'azul', 'azul'],
    10: ['azul', 'azul', 'azul', 'rojo', 'rojo', 'rojo'],
    11: ['rojo', 'azul', 'azul', 'rojo', 'rojo', 'azul'],
    12: ['rojo', 'azul', 'rojo', 'rojo', 'azul', 'rojo'],
    13: ['rojo', 'rojo', 'azul', 'rojo', 'rojo', 'azul'],
    14: ['rojo', 'rojo', 'azul', 'rojo', 'azul', 'rojo'],
    15: ['azul', 'rojo', 'rojo', 'azul', 'rojo', 'rojo'],
    16: [],  # Duplicado de 6
    17: ['rojo', 'azul', 'azul', 'rojo', 'azul', 'azul'],
    18: ['azul', 'azul', 'rojo', 'azul', 'rojo', 'rojo'],
    19: ['azul', 'azul', 'rojo', 'azul', 'azul', 'rojo'],
    20: ['azul', 'rojo', 'azul', 'azul', 'rojo', 'azul'],
    21: ['rojo', 'rojo', 'azul', 'rojo', 'rojo', 'rojo'],
    22: ['rojo', 'rojo', 'rojo', 'azul', 'rojo', 'rojo'],
    23: [],  # Duplicado de 11
    24: [],  # Duplicado de 5
    25: [],  # Duplicado de 18
    26: [],  # Duplicado de 6
}

# Diccionario de predicciones: clave = número de patrón, valor = lista de colores
PREDICCIONES = {
    1: ['azul', 'azul', 'azul', 'azul', 'azul', 'azul'],
    2: ['rojo', 'rojo', 'rojo', 'rojo', 'rojo', 'rojo'],
    3: ['rojo', 'rojo', 'azul', 'azul', 'rojo', 'rojo'],
    4: ['rojo', 'azul', 'rojo', 'azul', 'rojo', 'azul'],
    5: ['azul', 'rojo', 'azul', 'rojo', 'azul', 'rojo'],
    6: ['rojo', 'rojo', 'azul', 'rojo', 'azul', 'rojo'],
    7: ['rojo', 'azul', 'rojo', 'azul', 'rojo', 'azul'],
    8: ['rojo', 'azul', 'rojo', 'azul', 'rojo', 'azul'],
    9: ['azul', 'rojo', 'azul', 'rojo', 'azul', 'rojo'],
    10: ['rojo', 'azul', 'rojo', 'azul', 'rojo', 'azul'],
    11: ['rojo', 'rojo', 'azul', 'rojo', 'azul', 'rojo'],
    12: ['rojo', 'azul', 'azul', 'rojo', 'rojo', 'azul'],
    13: ['azul', 'rojo', 'azul', 'rojo', 'azul', 'rojo'],
    14: ['azul', 'azul', 'rojo', 'rojo', 'azul', 'rojo'],
    15: ['azul', 'azul', 'rojo', 'rojo', 'azul', 'azul'],
    16: ['rojo', 'rojo', 'azul', 'rojo', 'azul', 'rojo'],
    17: ['rojo', 'rojo', 'azul', 'rojo', 'azul', 'rojo'],
    18: ['rojo', 'rojo', 'azul', 'rojo', 'azul', 'rojo'],
    19: ['rojo', 'rojo', 'azul', 'rojo', 'azul', 'rojo'],
    20: ['rojo', 'rojo', 'azul', 'rojo', 'azul', 'rojo'],
    21: ['azul', 'azul', 'rojo', 'rojo', 'azul', 'rojo'],
    22: ['azul', 'azul', 'rojo', 'rojo', 'azul', 'rojo'],
    23: ['azul', 'rojo', 'azul', 'rojo', 'azul', 'rojo'],
    24: ['azul', 'rojo', 'azul', 'rojo', 'azul', 'rojo'],
    25: ['azul', 'azul', 'rojo', 'rojo', 'azul', 'rojo'],
    26: ['rojo', 'rojo', 'azul', 'rojo', 'azul', 'rojo'],
}

# Diccionario de nombres/descripciones
NOMBRES = {
    1: 'Banker fuerte (6 seguidos)',
    2: 'Player fuerte (6 seguidos)',
    3: 'Zigzag puro',
    4: 'Zigzag inverso',
    5: 'Patrón doble',
    6: 'Patrón doble',
    7: 'Patrón doble',
    8: 'Patrón doble inverso',
    9: '3-3 alternado',
    10: '3-3 alternado',
    11: 'Desordenado de repetición',
    12: 'Mixto balanceado',
    13: '2-1-2 patrón',
    14: '2-1-2 patrón',
    15: 'Similar 13 invertido',
    16: 'Triple intermedio',
    17: 'Alternancia desordenada',
    18: '2-3-1',
    19: '2-1 patrón',
    20: 'Escalonado',
    21: 'Final dominante',
    22: '3-1-1',
    23: '2-2-2 tipo espejo',
    24: 'Patrón espejo inverso',
    25: '3-2 tipo defensa',
    26: 'Triple de en medio',
}

def detectar_patrones(hist, captura_path, mesa, log_func):
    """
    Detecta todos los patrones definidos en PATRONES.
    Si el historial coincide con algún patrón, llama a log_func con la predicción correspondiente.
    """
    for num, patron in PATRONES.items():
        if not patron:
            continue  # Saltar patrones duplicados
        n = len(patron)
        hist_filtrado = [h for h in hist if h in ('rojo', 'azul')]
        if len(hist_filtrado) < n:
            continue
        if hist_filtrado[-n:] == patron:
            prediccion = PREDICCIONES[num]
            log_func(
                mesa,
                f"Patrón {num}: {NOMBRES[num]} detectado: {', '.join(hist_filtrado[-n:])}",
                captura_path,
                sugerencia_lista=prediccion
            )

# Funciones individuales para cada patrón (por compatibilidad con el sistema actual)
def detectar_patron_1(hist, captura_path, mesa, log_func):
    detectar_patrones(hist, captura_path, mesa, log_func)
def detectar_patron_2(hist, captura_path, mesa, log_func):
    detectar_patrones(hist, captura_path, mesa, log_func)
def detectar_patron_3(hist, captura_path, mesa, log_func):
    detectar_patrones(hist, captura_path, mesa, log_func)
def detectar_patron_4(hist, captura_path, mesa, log_func):
    detectar_patrones(hist, captura_path, mesa, log_func)
def detectar_patron_5(hist, captura_path, mesa, log_func):
    detectar_patrones(hist, captura_path, mesa, log_func)
def detectar_patron_6(hist, captura_path, mesa, log_func):
    detectar_patrones(hist, captura_path, mesa, log_func)
def detectar_patron_7(hist, captura_path, mesa, log_func):
    detectar_patrones(hist, captura_path, mesa, log_func)
def detectar_patron_8(hist, captura_path, mesa, log_func):
    detectar_patrones(hist, captura_path, mesa, log_func)
def detectar_patron_9(hist, captura_path, mesa, log_func):
    detectar_patrones(hist, captura_path, mesa, log_func)
def detectar_patron_10(hist, captura_path, mesa, log_func):
    detectar_patrones(hist, captura_path, mesa, log_func)
def detectar_patron_11(hist, captura_path, mesa, log_func):
    detectar_patrones(hist, captura_path, mesa, log_func)
def detectar_patron_12(hist, captura_path, mesa, log_func):
    detectar_patrones(hist, captura_path, mesa, log_func)
def detectar_patron_13(hist, captura_path, mesa, log_func):
    detectar_patrones(hist, captura_path, mesa, log_func)
def detectar_patron_14(hist, captura_path, mesa, log_func):
    detectar_patrones(hist, captura_path, mesa, log_func)
def detectar_patron_15(hist, captura_path, mesa, log_func):
    detectar_patrones(hist, captura_path, mesa, log_func)
def detectar_patron_16(hist, captura_path, mesa, log_func):
    detectar_patrones(hist, captura_path, mesa, log_func)
def detectar_patron_17(hist, captura_path, mesa, log_func):
    detectar_patrones(hist, captura_path, mesa, log_func)
def detectar_patron_18(hist, captura_path, mesa, log_func):
    detectar_patrones(hist, captura_path, mesa, log_func)
def detectar_patron_19(hist, captura_path, mesa, log_func):
    detectar_patrones(hist, captura_path, mesa, log_func)
def detectar_patron_20(hist, captura_path, mesa, log_func):
    detectar_patrones(hist, captura_path, mesa, log_func)
def detectar_patron_21(hist, captura_path, mesa, log_func):
    detectar_patrones(hist, captura_path, mesa, log_func)
def detectar_patron_22(hist, captura_path, mesa, log_func):
    detectar_patrones(hist, captura_path, mesa, log_func)
def detectar_patron_23(hist, captura_path, mesa, log_func):
    detectar_patrones(hist, captura_path, mesa, log_func)
def detectar_patron_24(hist, captura_path, mesa, log_func):
    detectar_patrones(hist, captura_path, mesa, log_func)
def detectar_patron_25(hist, captura_path, mesa, log_func):
    detectar_patrones(hist, captura_path, mesa, log_func)
def detectar_patron_26(hist, captura_path, mesa, log_func):
    detectar_patrones(hist, captura_path, mesa, log_func)

def invertir_secuencia(seq):
    return [('rojo' if c=='azul' else 'azul') for c in seq]

# Señal 1: 5 rojos seguidos (ignorando verdes)
# Detecta 5 rojos consecutivos. Sugerimos 5 apuestas a azul (cambio de tendencia esperado).
def detectar_senal_1(hist, captura_path, mesa, log_func):
    hist_filtrado = [h for h in hist if h in ('rojo', 'azul')]
    if len(hist_filtrado) < 5:
        return
    if all(h == 'rojo' for h in hist_filtrado[-5:]):
        sugerencia = ['azul']*5
        log_func(
            mesa,
            f"5 ROJOS CONSECUTIVOS detectados: {', '.join(hist_filtrado[-5:])}",
            captura_path,
            sugerencia_lista=sugerencia
        )

# Señal 1 AZUL: 5 azules seguidos (ignorando verdes)
# Detecta 5 azules consecutivos. Sugerimos 5 apuestas a rojo (cambio de tendencia esperado).
def detectar_senal_1_azul(hist, captura_path, mesa, log_func):
    hist_filtrado = [h for h in hist if h in ('rojo', 'azul')]
    if len(hist_filtrado) < 5:
        return
    if all(h == 'azul' for h in hist_filtrado[-5:]):
        sugerencia = ['rojo']*5
        log_func(
            mesa,
            f"5 AZULES CONSECUTIVOS detectados: {', '.join(hist_filtrado[-5:])}",
            captura_path,
            sugerencia_lista=sugerencia
        )

# Señal 2: intercalado mínimo 5 veces, empezando en rojo (ignorando verdes)
# Detecta alternancia rojo-azul al menos 5 veces, empezando en rojo. Sugerimos seguir alternando 5 veces más.
def detectar_senal_2(hist, captura_path, mesa, log_func):
    hist_filtrado = [h for h in hist if h in ('rojo', 'azul')]
    if len(hist_filtrado) < 6:
        return
    intercalado_rojo = True
    for i in range(-5, 0):
        if hist_filtrado[i] == hist_filtrado[i-1]:
            intercalado_rojo = False
            break
    if intercalado_rojo and hist_filtrado[-6] == 'rojo':
        sugerencia = ['rojo', 'azul', 'rojo', 'azul', 'rojo']
        log_func(
            mesa,
            f"PATRÓN INTERCALADO ROJO-AZUL detectado: {', '.join(hist_filtrado[-6:])}",
            captura_path,
            sugerencia_lista=sugerencia
        )

# Señal 2 AZUL: intercalado mínimo 5 veces, empezando en azul (ignorando verdes)
# Detecta alternancia azul-rojo al menos 5 veces, empezando en azul. Sugerimos seguir alternando 5 veces más.
def detectar_senal_2_azul(hist, captura_path, mesa, log_func):
    hist_filtrado = [h for h in hist if h in ('rojo', 'azul')]
    if len(hist_filtrado) < 6:
        return
    intercalado_azul = True
    for i in range(-5, 0):
        if hist_filtrado[i] == hist_filtrado[i-1]:
            intercalado_azul = False
            break
    if intercalado_azul and hist_filtrado[-6] == 'azul':
        sugerencia = ['azul', 'rojo', 'azul', 'rojo', 'azul']
        log_func(
            mesa,
            f"PATRÓN INTERCALADO AZUL-ROJO detectado: {', '.join(hist_filtrado[-6:])}",
            captura_path,
            sugerencia_lista=sugerencia
        )

# Señal 3: patrón tipo rojo, rojo, azul, rojo, rojo, azul, rojo, rojo (ignorando verdes)
# Detecta el patrón rojo, rojo, azul, rojo, rojo, azul, rojo, rojo. Sugerimos 5 apuestas a rojo (tendencia de racha).
def detectar_senal_3(hist, captura_path, mesa, log_func):
    hist_filtrado = [h for h in hist if h in ('rojo', 'azul')]
    if len(hist_filtrado) < 8:
        return
    patron = hist_filtrado[-8:]
    if patron[0] == patron[1] == patron[3] == patron[4] == patron[6] == patron[7] == 'rojo' and \
       patron[2] == patron[5] == 'azul':
        sugerencia = ['rojo']*5
        log_func(
            mesa,
            f"PATRÓN ROJO-ROJO-AZUL detectado: {', '.join(patron)}",
            captura_path,
            sugerencia_lista=sugerencia
        )

# Señal 3 AZUL: patrón tipo azul, azul, rojo, azul, azul, rojo, azul, azul (ignorando verdes)
# Detecta el patrón azul, azul, rojo, azul, azul, rojo, azul, azul. Sugerimos 5 apuestas a azul (tendencia de racha).
def detectar_senal_3_azul(hist, captura_path, mesa, log_func):
    hist_filtrado = [h for h in hist if h in ('rojo', 'azul')]
    if len(hist_filtrado) < 8:
        return
    patron = hist_filtrado[-8:]
    if patron[0] == patron[1] == patron[3] == patron[4] == patron[6] == patron[7] == 'azul' and \
       patron[2] == patron[5] == 'rojo':
        sugerencia = ['azul']*5
        log_func(
            mesa,
            f"PATRÓN AZUL-AZUL-ROJO detectado: {', '.join(patron)}",
            captura_path,
            sugerencia_lista=sugerencia
        )

# Señal 4: Escalera ascendente (4 iguales y 1 diferente al final)
# Detecta una secuencia de 4 resultados iguales seguidos de 1 diferente (ejemplo: rojo, rojo, rojo, rojo, azul).
# Sugerencia: Apostar varias veces al color que acaba de aparecer (el diferente).
def detectar_senal_4(hist, captura_path, mesa, log_func):
    hist_filtrado = [h for h in hist if h in ('rojo', 'azul')]
    if len(hist_filtrado) < 5:
        return
    patron = hist_filtrado[-5:]
    if patron[0] == patron[1] == patron[2] == patron[3] and patron[4] != patron[3]:
        sugerencia = [patron[4]]*3
        log_func(
            mesa,
            f"ESCALERA ASCENDENTE detectada: {', '.join(patron)}",
            captura_path,
            sugerencia_lista=sugerencia
        )

# Señal 4 AZUL: Escalera ascendente invertida
# Igual que la anterior, pero aplica para cualquier color dominante y su opuesto.
def detectar_senal_4_azul(hist, captura_path, mesa, log_func):
    hist_filtrado = [h for h in hist if h in ('rojo', 'azul')]
    if len(hist_filtrado) < 5:
        return
    patron = hist_filtrado[-5:]
    if patron[0] == patron[1] == patron[2] == patron[3] and patron[4] != patron[3]:
        sugerencia = [patron[4]]*3
        log_func(
            mesa,
            f"ESCALERA ASCENDENTE INVERTIDA detectada: {', '.join(patron)}",
            captura_path,
            sugerencia_lista=sugerencia
        )

# Señal 5: Doble doble y uno diferente
# Detecta dos pares de colores seguidos de un color diferente (ejemplo: rojo, rojo, azul, azul, rojo).
# Sugerencia: Apostar a que se repite el último color.
def detectar_senal_5(hist, captura_path, mesa, log_func):
    hist_filtrado = [h for h in hist if h in ('rojo', 'azul')]
    if len(hist_filtrado) < 5:
        return
    patron = hist_filtrado[-5:]
    if patron[0] == patron[1] and patron[2] == patron[3] and patron[4] != patron[3]:
        sugerencia = [patron[4]]*2
        log_func(
            mesa,
            f"DOBLE DOBLE Y UNO DIFERENTE detectado: {', '.join(patron)}",
            captura_path,
            sugerencia_lista=sugerencia
        )

# Señal 5 AZUL: Doble doble y uno diferente invertido
# Igual que la anterior, pero aplica para cualquier combinación de pares y un diferente.
def detectar_senal_5_azul(hist, captura_path, mesa, log_func):
    hist_filtrado = [h for h in hist if h in ('rojo', 'azul')]
    if len(hist_filtrado) < 5:
        return
    patron = hist_filtrado[-5:]
    if patron[0] == patron[1] and patron[2] == patron[3] and patron[4] != patron[3]:
        sugerencia = [patron[4]]*2
        log_func(
            mesa,
            f"DOBLE DOBLE Y UNO DIFERENTE INVERTIDO detectado: {', '.join(patron)}",
            captura_path,
            sugerencia_lista=sugerencia
        )

# Señal 6: Tres pares alternados
# Detecta tres pares de colores alternados (ejemplo: rojo, rojo, azul, azul, rojo, rojo).
# Sugerencia: Apostar a que se repite el último par.
def detectar_senal_6(hist, captura_path, mesa, log_func):
    hist_filtrado = [h for h in hist if h in ('rojo', 'azul')]
    if len(hist_filtrado) < 6:
        return
    patron = hist_filtrado[-6:]
    if patron[0] == patron[1] and patron[2] == patron[3] and patron[4] == patron[5] and len(set([patron[0], patron[2], patron[4]])) == 3:
        sugerencia = [patron[4]]*2
        log_func(
            mesa,
            f"TRES PARES ALTERNADOS detectado: {', '.join(patron)}",
            captura_path,
            sugerencia_lista=sugerencia
        )

# Señal 6 AZUL: Tres pares alternados invertido
# Igual que la anterior, pero aplica para cualquier secuencia de tres pares alternados.
def detectar_senal_6_azul(hist, captura_path, mesa, log_func):
    hist_filtrado = [h for h in hist if h in ('rojo', 'azul')]
    if len(hist_filtrado) < 6:
        return
    patron = hist_filtrado[-6:]
    if patron[0] == patron[1] and patron[2] == patron[3] and patron[4] == patron[5] and len(set([patron[0], patron[2], patron[4]])) == 3:
        sugerencia = [patron[4]]*2
        log_func(
            mesa,
            f"TRES PARES ALTERNADOS INVERTIDO detectado: {', '.join(patron)}",
            captura_path,
            sugerencia_lista=sugerencia
        )

# Señal 7: Racha de 3, cambio, racha de 3, cambio
# Detecta una racha de 3 de un color, cambio, racha de 3 del otro color, y cambio nuevamente (ejemplo: rojo, rojo, rojo, azul, azul, azul, rojo).
# Sugerencia: Apostar a que se inicia una nueva racha del color que acaba de aparecer.
def detectar_senal_7(hist, captura_path, mesa, log_func):
    hist_filtrado = [h for h in hist if h in ('rojo', 'azul')]
    if len(hist_filtrado) < 7:
        return
    patron = hist_filtrado[-7:]
    if patron[0] == patron[1] == patron[2] and patron[3] != patron[2] and patron[4] == patron[5] == patron[3] and patron[6] != patron[5]:
        sugerencia = [patron[6]]*2
        log_func(
            mesa,
            f"RACHA DE 3, CAMBIO, RACHA DE 3, CAMBIO detectado: {', '.join(patron)}",
            captura_path,
            sugerencia_lista=sugerencia
        )

# Señal 7 AZUL: Racha de 3, cambio, racha de 3, cambio invertido
# Igual que la anterior, pero aplica para cualquier color dominante.
def detectar_senal_7_azul(hist, captura_path, mesa, log_func):
    hist_filtrado = [h for h in hist if h in ('rojo', 'azul')]
    if len(hist_filtrado) < 7:
        return
    patron = hist_filtrado[-7:]
    if patron[0] == patron[1] == patron[2] and patron[3] != patron[2] and patron[4] == patron[5] == patron[3] and patron[6] != patron[5]:
        sugerencia = [patron[6]]*2
        log_func(
            mesa,
            f"RACHA DE 3, CAMBIO, RACHA DE 3, CAMBIO INVERTIDO detectado: {', '.join(patron)}",
            captura_path,
            sugerencia_lista=sugerencia
        )

# Señal 8: Dos rachas de 4
# Detecta dos rachas de 4 del mismo color, pero de colores opuestos (ejemplo: rojo, rojo, rojo, rojo, azul, azul, azul, azul).
# Sugerencia: Apostar a que inicia una nueva racha del primer color.
def detectar_senal_8(hist, captura_path, mesa, log_func):
    hist_filtrado = [h for h in hist if h in ('rojo', 'azul')]
    if len(hist_filtrado) < 8:
        return
    patron = hist_filtrado[-8:]
    if patron[0] == patron[1] == patron[2] == patron[3] and patron[4] == patron[5] == patron[6] == patron[7] and patron[0] != patron[4]:
        sugerencia = [patron[0]]*2
        log_func(
            mesa,
            f"DOS RACHAS DE 4 detectado: {', '.join(patron)}",
            captura_path,
            sugerencia_lista=sugerencia
        )

# Señal 8 AZUL: Dos rachas de 4 invertido
# Igual que la anterior, pero aplica para cualquier color dominante.
def detectar_senal_8_azul(hist, captura_path, mesa, log_func):
    hist_filtrado = [h for h in hist if h in ('rojo', 'azul')]
    if len(hist_filtrado) < 8:
        return
    patron = hist_filtrado[-8:]
    if patron[0] == patron[1] == patron[2] == patron[3] and patron[4] == patron[5] == patron[6] == patron[7] and patron[0] != patron[4]:
        sugerencia = [patron[4]]*2
        log_func(
            mesa,
            f"DOS RACHAS DE 4 INVERTIDO detectado: {', '.join(patron)}",
            captura_path,
            sugerencia_lista=sugerencia
        )

# Señal 9: Patrón espejo
# Detecta un patrón simétrico de 4 y 4 (ejemplo: rojo, azul, azul, rojo, rojo, azul, azul, rojo).
# Sugerencia: Apostar a que se repite el patrón desde el inicio.
def detectar_senal_9(hist, captura_path, mesa, log_func):
    hist_filtrado = [h for h in hist if h in ('rojo', 'azul')]
    if len(hist_filtrado) < 8:
        return
    patron = hist_filtrado[-8:]
    if patron[0] == patron[7] and patron[1] == patron[6] and patron[2] == patron[5] and patron[3] == patron[4]:
        sugerencia = [patron[0], patron[1], patron[2], patron[3]]
        log_func(
            mesa,
            f"PATRÓN ESPEJO detectado: {', '.join(patron)}",
            captura_path,
            sugerencia_lista=sugerencia
        )

# Señal 9 AZUL: Patrón espejo invertido
# Igual que la anterior, pero aplica para cualquier combinación simétrica.
def detectar_senal_9_azul(hist, captura_path, mesa, log_func):
    hist_filtrado = [h for h in hist if h in ('rojo', 'azul')]
    if len(hist_filtrado) < 8:
        return
    patron = hist_filtrado[-8:]
    if patron[0] == patron[7] and patron[1] == patron[6] and patron[2] == patron[5] and patron[3] == patron[4]:
        sugerencia = [patron[4], patron[5], patron[6], patron[7]]
        log_func(
            mesa,
            f"PATRÓN ESPEJO INVERTIDO detectado: {', '.join(patron)}",
            captura_path,
            sugerencia_lista=sugerencia
        )

# Señal 10: Alternancia con ruptura al final
# Detecta alternancia perfecta de colores con una ruptura al final (ejemplo: azul, rojo, azul, rojo, azul, rojo, azul, azul).
# Sugerencia: Apostar a que se mantiene la ruptura o vuelve la alternancia.
def detectar_senal_10(hist, captura_path, mesa, log_func):
    hist_filtrado = [h for h in hist if h in ('rojo', 'azul')]
    if len(hist_filtrado) < 8:
        return
    patron = hist_filtrado[-8:]
    if patron[0] != patron[1] and patron[1] != patron[2] and patron[2] != patron[3] and patron[3] != patron[4] and patron[4] != patron[5] and patron[5] != patron[6] and patron[6] == patron[7]:
        sugerencia = [patron[7]]*2
        log_func(
            mesa,
            f"ALTERNANCIA CON RUPTURA AL FINAL detectada: {', '.join(patron)}",
            captura_path,
            sugerencia_lista=sugerencia
        )

# Señal 10 AZUL: Alternancia con ruptura al final invertida
# Igual que la anterior, pero aplica para cualquier alternancia y ruptura final.
def detectar_senal_10_azul(hist, captura_path, mesa, log_func):
    hist_filtrado = [h for h in hist if h in ('rojo', 'azul')]
    if len(hist_filtrado) < 8:
        return
    patron = hist_filtrado[-8:]
    if patron[0] != patron[1] and patron[1] != patron[2] and patron[2] != patron[3] and patron[3] != patron[4] and patron[4] != patron[5] and patron[5] != patron[6] and patron[6] == patron[7]:
        sugerencia = [patron[7]]*2
        log_func(
            mesa,
            f"ALTERNANCIA CON RUPTURA AL FINAL INVERTIDA detectada: {', '.join(patron)}",
            captura_path,
            sugerencia_lista=sugerencia
        )

# Señal 11: Escalera descendente (4 alternados y 1 igual al final)
# Detecta una alternancia de 4 movimientos y el último repite el color anterior (ejemplo: rojo, azul, rojo, azul, azul).
# Sugerencia: Apostar a que se mantiene la racha del último color.
def detectar_senal_11(hist, captura_path, mesa, log_func):
    hist_filtrado = [h for h in hist if h in ('rojo', 'azul')]
    if len(hist_filtrado) < 5:
        return
    patron = hist_filtrado[-5:]
    if patron[0] != patron[1] and patron[1] != patron[2] and patron[2] != patron[3] and patron[3] == patron[4]:
        sugerencia = [patron[4]]*2
        log_func(
            mesa,
            f"ESCALERA DESCENDENTE detectada: {', '.join(patron)}",
            captura_path,
            sugerencia_lista=sugerencia
        )

# Señal 11 AZUL: Escalera descendente invertida
# Igual que la anterior, pero aplica para cualquier alternancia y repetición final.
def detectar_senal_11_azul(hist, captura_path, mesa, log_func):
    hist_filtrado = [h for h in hist if h in ('rojo', 'azul')]
    if len(hist_filtrado) < 5:
        return
    patron = hist_filtrado[-5:]
    if patron[0] != patron[1] and patron[1] != patron[2] and patron[2] != patron[3] and patron[3] == patron[4]:
        sugerencia = [patron[4]]*2
        log_func(
            mesa,
            f"ESCALERA DESCENDENTE INVERTIDA detectada: {', '.join(patron)}",
            captura_path,
            sugerencia_lista=sugerencia
        )

# Señal 12: Doble triple (tres de un color, tres del otro)
# Detecta tres de un color seguidos de tres del otro (ejemplo: rojo, rojo, rojo, azul, azul, azul).
# Sugerencia: Apostar a que inicia una nueva racha del primer color.
def detectar_senal_12(hist, captura_path, mesa, log_func):
    hist_filtrado = [h for h in hist if h in ('rojo', 'azul')]
    if len(hist_filtrado) < 6:
        return
    patron = hist_filtrado[-6:]
    if patron[0] == patron[1] == patron[2] and patron[3] == patron[4] == patron[5] and patron[0] != patron[3]:
        sugerencia = [patron[0]]*2
        log_func(
            mesa,
            f"DOBLE TRIPLE detectado: {', '.join(patron)}",
            captura_path,
            sugerencia_lista=sugerencia
        )

# Señal 12 AZUL: Doble triple invertido
# Igual que la anterior, pero aplica para cualquier color dominante.
def detectar_senal_12_azul(hist, captura_path, mesa, log_func):
    hist_filtrado = [h for h in hist if h in ('rojo', 'azul')]
    if len(hist_filtrado) < 6:
        return
    patron = hist_filtrado[-6:]
    if patron[0] == patron[1] == patron[2] and patron[3] == patron[4] == patron[5] and patron[0] != patron[3]:
        sugerencia = [patron[3]]*2
        log_func(
            mesa,
            f"DOBLE TRIPLE INVERTIDO detectado: {', '.join(patron)}",
            captura_path,
            sugerencia_lista=sugerencia
        )

# Señal 13: Sandwich (color en extremos y centro, otro color en pares intermedios)
# Ejemplo: rojo, azul, azul, rojo, azul, azul, rojo
# Sugerencia: Apostar a que se repite el color de los extremos.
def detectar_senal_13(hist, captura_path, mesa, log_func):
    hist_filtrado = [h for h in hist if h in ('rojo', 'azul')]
    if len(hist_filtrado) < 7:
        return
    patron = hist_filtrado[-7:]
    if patron[0] == patron[3] == patron[6] and patron[1] == patron[2] == patron[4] == patron[5] and patron[0] != patron[1]:
        sugerencia = [patron[0]]*2
        log_func(
            mesa,
            f"SANDWICH detectado: {', '.join(patron)}",
            captura_path,
            sugerencia_lista=sugerencia
        )

# Señal 13 AZUL: Sandwich invertido
# Igual que la anterior, pero aplica para cualquier combinación de colores.
def detectar_senal_13_azul(hist, captura_path, mesa, log_func):
    hist_filtrado = [h for h in hist if h in ('rojo', 'azul')]
    if len(hist_filtrado) < 7:
        return
    patron = hist_filtrado[-7:]
    if patron[0] == patron[3] == patron[6] and patron[1] == patron[2] == patron[4] == patron[5] and patron[0] != patron[1]:
        sugerencia = [patron[1]]*2
        log_func(
            mesa,
            f"SANDWICH INVERTIDO detectado: {', '.join(patron)}",
            captura_path,
            sugerencia_lista=sugerencia
        )

# Señal 14: Palíndromo (secuencia simétrica)
# Ejemplo: rojo, azul, azul, rojo, azul, azul, rojo
# Sugerencia: Apostar a que se repite el patrón desde el inicio.
def detectar_senal_14(hist, captura_path, mesa, log_func):
    hist_filtrado = [h for h in hist if h in ('rojo', 'azul')]
    if len(hist_filtrado) < 7:
        return
    patron = hist_filtrado[-7:]
    if patron == patron[::-1]:
        sugerencia = patron[:3]
        log_func(
            mesa,
            f"PALÍNDROMO detectado: {', '.join(patron)}",
            captura_path,
            sugerencia_lista=sugerencia
        )

# Señal 14 AZUL: Palíndromo invertido
# Igual que la anterior, pero aplica para cualquier secuencia simétrica.
def detectar_senal_14_azul(hist, captura_path, mesa, log_func):
    hist_filtrado = [h for h in hist if h in ('rojo', 'azul')]
    if len(hist_filtrado) < 7:
        return
    patron = hist_filtrado[-7:]
    if patron == patron[::-1]:
        sugerencia = patron[-3:]
        log_func(
            mesa,
            f"PALÍNDROMO INVERTIDO detectado: {', '.join(patron)}",
            captura_path,
            sugerencia_lista=sugerencia
        )

# Señal 15: Racha creciente (corta, larga, corta)
# Ejemplo: rojo, azul, azul, rojo, rojo, rojo, azul, azul
# Sugerencia: Apostar a que se repite la racha corta.
def detectar_senal_15(hist, captura_path, mesa, log_func):
    hist_filtrado = [h for h in hist if h in ('rojo', 'azul')]
    if len(hist_filtrado) < 8:
        return
    patron = hist_filtrado[-8:]
    if patron[0] != patron[1] and patron[2] == patron[3] == patron[4] and patron[5] != patron[6] and patron[6] == patron[7]:
        sugerencia = [patron[6], patron[7]]
        log_func(
            mesa,
            f"RACHA CRECIENTE detectada: {', '.join(patron)}",
            captura_path,
            sugerencia_lista=sugerencia
        )

# Señal 15 AZUL: Racha creciente invertida
# Igual que la anterior, pero aplica para cualquier combinación de rachas cortas y largas.
def detectar_senal_15_azul(hist, captura_path, mesa, log_func):
    hist_filtrado = [h for h in hist if h in ('rojo', 'azul')]
    if len(hist_filtrado) < 8:
        return
    patron = hist_filtrado[-8:]
    if patron[0] != patron[1] and patron[2] == patron[3] == patron[4] and patron[5] != patron[6] and patron[6] == patron[7]:
        sugerencia = [patron[0], patron[1]]
        log_func(
            mesa,
            f"RACHA CRECIENTE INVERTIDA detectada: {', '.join(patron)}",
            captura_path,
            sugerencia_lista=sugerencia
        )

# Señal 16: Doble espejo (dos patrones espejo de 4 movimientos)
# Ejemplo: rojo, azul, azul, rojo, rojo, azul, azul, rojo
# Sugerencia: Apostar a que se repite el patrón.
def detectar_senal_16(hist, captura_path, mesa, log_func):
    hist_filtrado = [h for h in hist if h in ('rojo', 'azul')]
    if len(hist_filtrado) < 8:
        return
    patron = hist_filtrado[-8:]
    if patron[:4] == patron[4:] or patron[:4] == patron[4:][::-1]:
        sugerencia = patron[:4]
        log_func(
            mesa,
            f"DOBLE ESPEJO detectado: {', '.join(patron)}",
            captura_path,
            sugerencia_lista=sugerencia
        )

# Señal 16 AZUL: Doble espejo invertido
# Igual que la anterior, pero aplica para cualquier combinación de patrones espejo.
def detectar_senal_16_azul(hist, captura_path, mesa, log_func):
    hist_filtrado = [h for h in hist if h in ('rojo', 'azul')]
    if len(hist_filtrado) < 8:
        return
    patron = hist_filtrado[-8:]
    if patron[:4] == patron[4:] or patron[:4] == patron[4:][::-1]:
        sugerencia = patron[4:]
        log_func(
            mesa,
            f"DOBLE ESPEJO INVERTIDO detectado: {', '.join(patron)}",
            captura_path,
            sugerencia_lista=sugerencia
        ) 