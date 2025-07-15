# Archivo con los patrones de detección de señales para Baccarat

def invertir_secuencia(seq):
    return [('rojo' if c=='azul' else 'azul') for c in seq]

# Señal 1: 5 rojos seguidos (ignorando verdes)
def detectar_senal_1(hist, captura_path, mesa, log_func):
    hist_filtrado = [h for h in hist if h in ('rojo', 'azul')]
    if len(hist_filtrado) < 5:
        return
    if all(h == 'rojo' for h in hist_filtrado[-5:]):
        sugerencia = ['azul']*6
        log_func(
            mesa,
            f"5 ROJOS CONSECUTIVOS detectados: {', '.join(hist_filtrado[-7:])}",
            captura_path,
            sugerencia_lista=sugerencia
        )

# Señal 1 AZUL: 5 azules seguidos (ignorando verdes)
def detectar_senal_1_azul(hist, captura_path, mesa, log_func):
    hist_filtrado = [h for h in hist if h in ('rojo', 'azul')]
    if len(hist_filtrado) < 5:
        return
    if all(h == 'azul' for h in hist_filtrado[-5:]):
        sugerencia = ['rojo']*6
        log_func(
            mesa,
            f"5 AZULES CONSECUTIVOS detectados: {', '.join(hist_filtrado[-7:])}",
            captura_path,
            sugerencia_lista=sugerencia
        )

# Señal 2: intercalado mínimo 5 veces, empezando en rojo (ignorando verdes)
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
        sugerencia = ['rojo', 'azul', 'rojo', 'azul', 'rojo', 'azul']
        log_func(
            mesa,
            f"PATRÓN INTERCALADO ROJO-AZUL detectado: {', '.join(hist_filtrado[-7:])}",
            captura_path,
            sugerencia_lista=sugerencia
        )

# Señal 2 AZUL: intercalado mínimo 5 veces, empezando en azul (ignorando verdes)
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
        sugerencia = ['azul', 'rojo', 'azul', 'rojo', 'azul', 'rojo']
        log_func(
            mesa,
            f"PATRÓN INTERCALADO AZUL-ROJO detectado: {', '.join(hist_filtrado[-7:])}",
            captura_path,
            sugerencia_lista=sugerencia
        )

# Señal 3: patrón tipo rojo, rojo, azul, rojo, rojo, azul, rojo, rojo (ignorando verdes)
def detectar_senal_3(hist, captura_path, mesa, log_func):
    hist_filtrado = [h for h in hist if h in ('rojo', 'azul')]
    if len(hist_filtrado) < 8:
        return
    patron = hist_filtrado[-8:]
    if patron[0] == patron[1] == patron[3] == patron[4] == patron[6] == patron[7] == 'rojo' and \
       patron[2] == patron[5] == 'azul':
        final = patron[-1]
        if final == 'rojo':
            sugerencia = ['rojo', 'azul', 'rojo', 'rojo', 'rojo']
        else:
            sugerencia = ['azul', 'rojo', 'rojo', 'rojo', 'rojo', 'rojo']
        log_func(
            mesa,
            f"PATRÓN ROJO-ROJO-AZUL detectado: {', '.join(patron)}",
            captura_path,
            sugerencia_lista=sugerencia
        )

# Señal 3 AZUL: patrón tipo azul, azul, rojo, azul, azul, rojo, azul, azul (ignorando verdes)
def detectar_senal_3_azul(hist, captura_path, mesa, log_func):
    hist_filtrado = [h for h in hist if h in ('rojo', 'azul')]
    if len(hist_filtrado) < 8:
        return
    patron = hist_filtrado[-8:]
    if patron[0] == patron[1] == patron[3] == patron[4] == patron[6] == patron[7] == 'azul' and \
       patron[2] == patron[5] == 'rojo':
        final = patron[-1]
        if final == 'azul':
            sugerencia = ['azul', 'rojo', 'azul', 'azul', 'azul']
        else:
            sugerencia = ['rojo', 'azul', 'azul', 'azul', 'azul', 'azul']
        log_func(
            mesa,
            f"PATRÓN AZUL-AZUL-ROJO detectado: {', '.join(patron)}",
            captura_path,
            sugerencia_lista=sugerencia
        ) 