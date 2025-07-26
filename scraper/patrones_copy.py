# Archivo con los patrones de detección de señales para Baccarat

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