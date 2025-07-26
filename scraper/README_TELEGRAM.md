# Sistema de Monitoreo Baccarat con Telegram

## Descripción
Este sistema automatiza el monitoreo de resultados de Baccarat en Stake.com y envía automáticamente los resultados y señales a chats específicos de Telegram.

## Funcionalidades

### 📊 Chat de Estadísticas
- **ID del Chat**: `-1002465111695`
- **Contenido**: Cada resultado detectado de la mesa
- **Formato del mensaje**:
  ```
  RESULTADO MESA 1
  Color: ROJO
  Hora: 14:30:25
  Resultado #1
  ```

### 🚨 Chat de Señales
- **ID del Chat**: `-1002539477075`
- **Contenido**: Señales de rachas significativas (3+ resultados consecutivos)
- **Formato del mensaje**:
  ```
  SEÑAL DE RACHA
  Color: AZUL
  Racha: 3 resultados consecutivos
  Hora: 14:35:10
  Considerar cambio de tendencia
  ```

## Archivos del Sistema

### `main_copy.py` (Archivo Principal)
- **Función**: Script principal de monitoreo con integración Telegram
- **Características**:
  - Navegación automática a Stake.com
  - Login automático
  - Monitoreo de resultados en tiempo real
  - Envío automático de mensajes a Telegram
  - Detección de rachas y señales

### `send_message.py` (Archivo de Prueba Original)
- **Función**: Script simple para probar envío de mensajes
- **Uso**: Solo para pruebas básicas

### `test_telegram.py` (Archivo de Prueba)
- **Función**: Verificar que la conexión con Telegram funciona
- **Uso**: Ejecutar antes del monitoreo principal

## Configuración

### Token de Telegram
```python
TELEGRAM_TOKEN = "7792602918:AAFW7atIz-5qNaHVItDPv1C-hd2M679WA8s"
```

### Chats Configurados
```python
TELEGRAM_CHATS = {
    "estadisticas": "-1002465111695",
    "señales": "-1002539477075"
}
```

## Cómo Usar

### 1. Prueba de Conexión
```bash
python test_telegram.py
```
Este comando enviará mensajes de prueba a ambos chats para verificar que la conexión funciona.

### 2. Monitoreo Principal
```bash
python main_copy.py
```
Este comando iniciará el monitoreo completo con envío automático de mensajes.

## Logs del Sistema

### Logs de Consola
- **Formato**: Sin emojis (compatible con consola)
- **Información**:
  - Progreso de navegación
  - Resultados detectados
  - Estado de envío de mensajes
  - Rachas detectadas

### Logs de Telegram
- **Formato**: Con formato HTML (negritas, cursivas)
- **Información**:
  - Resultados en tiempo real
  - Señales de rachas
  - Mensajes de inicio y fin
  - Errores del sistema

## Detección de Rachas

### Lógica de Rachas
- **Racha**: Secuencia de resultados del mismo color
- **Señal**: Se envía cuando hay 3 o más resultados consecutivos
- **Prevención de Duplicados**: No se envía la misma señal múltiples veces

### Ejemplo de Racha
```
Resultado 1: ROJO
Resultado 2: ROJO  
Resultado 3: ROJO  ← SEÑAL ENVIADA
Resultado 4: ROJO  ← SEÑAL ENVIADA
Resultado 5: AZUL  ← Nueva racha
```

## Estructura de Carpetas

```
capturas/
├── paso_01_navegacion/
├── paso_02_login/
├── paso_06_casino/
├── paso_10_juego/
├── paso_15_pantalla_completa/
├── paso_16_calibracion/
├── paso_17_monitoreo/     ← Capturas de resultados
└── debug/
```

## Mensajes Automáticos

### Al Iniciar
```
MONITOREO INICIADO
Mesa: Baccarat Mesa 1
Hora: 14:30:00
Estado: Monitoreando resultados...
```

### Al Finalizar
```
MONITOREO FINALIZADO
Total de resultados: 25
Último color: ROJO
Rachas finales:
• Rojo: 2
• Azul: 0
• Verde: 0
Hora: 15:00:00
```

### En Caso de Error
```
ERROR EN MONITOREO
Error: Connection timeout...
Hora: 14:45:30
```

## Dependencias

```python
import requests          # Para API de Telegram
import datetime          # Para timestamps
import numpy as np       # Para análisis de imágenes
from PIL import Image    # Para procesamiento de imágenes
from playwright.sync_api import sync_playwright  # Para automatización web
```

## Notas Importantes

1. **Sin Emojis**: Los logs de consola no usan emojis para compatibilidad
2. **Formato HTML**: Los mensajes de Telegram usan formato HTML para mejor presentación
3. **Prevención de Spam**: Las señales de racha no se duplican
4. **Manejo de Errores**: Errores de conexión no detienen el monitoreo
5. **Capturas**: Se guardan automáticamente todas las capturas de resultados

## Troubleshooting

### Error de Conexión Telegram
- Verificar que el token sea válido
- Verificar que el bot esté agregado a los chats
- Verificar conexión a internet

### Error de Detección
- Verificar que el área de captura sea correcta
- Revisar las capturas en `capturas/paso_17_monitoreo/`
- Ajustar coordenadas si es necesario

### Error de Navegación
- Verificar credenciales de Stake.com
- Verificar que el sitio esté accesible
- Revisar logs de navegación 