#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de prueba para verificar la funcionalidad de Telegram
"""

import requests
from datetime import datetime

# --- Configuración Telegram ---
TELEGRAM_TOKEN = "7792602918:AAFW7atIz-5qNaHVItDPv1C-hd2M679WA8s"
TELEGRAM_CHATS = {
    "estadisticas": "-1002465111695",
    "señales": "-1002539477075"
}
TELEGRAM_EXTRA_ID = "6078161114"  # Nuevo ID adicional

def enviar_mensaje_telegram(token, chat_id, mensaje):
    """Envía un mensaje a un chat específico de Telegram."""
    try:
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        params = {
            "chat_id": chat_id,
            "text": mensaje,
            "parse_mode": "HTML"
        }
        response = requests.get(url, params=params)
        
        if response.status_code == 200:
            print(f"[TELEGRAM] Mensaje enviado exitosamente a {chat_id}")
            return True
        else:
            print(f"[TELEGRAM] Error al enviar mensaje: {response.status_code} - {response.text}")
            return False
    except Exception as e:
        print(f"[TELEGRAM] Error en envío: {e}")
        return False

def enviar_resultado_estadisticas(color, numero_resultado):
    """Envía el resultado de la mesa al chat de estadísticas y al ID extra."""
    timestamp = datetime.now().strftime("%H:%M:%S")
    mensaje = f"<b>RESULTADO MESA 1</b>\n"
    mensaje += f"Color: <b>{color.upper()}</b>\n"
    mensaje += f"Hora: {timestamp}\n"
    mensaje += f"Resultado #{numero_resultado}"
    
    exito1 = enviar_mensaje_telegram(TELEGRAM_TOKEN, TELEGRAM_CHATS["estadisticas"], mensaje)
    exito2 = enviar_mensaje_telegram(TELEGRAM_TOKEN, TELEGRAM_EXTRA_ID, mensaje)
    return exito1 and exito2

def enviar_señal_rachas(color, racha_actual):
    """Envía una señal cuando se detecta una racha significativa, también al ID extra."""
    timestamp = datetime.now().strftime("%H:%M:%S")
    mensaje = f"<b>SEÑAL DE RACHA</b>\n"
    mensaje += f"Color: <b>{color.upper()}</b>\n"
    mensaje += f"Racha: {racha_actual} resultados consecutivos\n"
    mensaje += f"Hora: {timestamp}\n"
    mensaje += f"<i>Considerar cambio de tendencia</i>"
    
    exito1 = enviar_mensaje_telegram(TELEGRAM_TOKEN, TELEGRAM_CHATS["señales"], mensaje)
    exito2 = enviar_mensaje_telegram(TELEGRAM_TOKEN, TELEGRAM_EXTRA_ID, mensaje)
    return exito1 and exito2

def main():
    print("=== PRUEBA DE FUNCIONALIDAD TELEGRAM ===")
    print(f"Token: {TELEGRAM_TOKEN[:20]}...")
    print(f"Chat Estadísticas: {TELEGRAM_CHATS['estadisticas']}")
    print(f"Chat Señales: {TELEGRAM_CHATS['señales']}")
    print()
    
    # Prueba 1: Mensaje de inicio
    print("1. Enviando mensaje de inicio a estadísticas...")
    mensaje_inicio = f"<b>PRUEBA DE CONEXIÓN</b>\n"
    mensaje_inicio += f"Script: Test Telegram\n"
    mensaje_inicio += f"Hora: {datetime.now().strftime('%H:%M:%S')}\n"
    mensaje_inicio += f"Estado: Verificando conexión..."
    
    if enviar_mensaje_telegram(TELEGRAM_TOKEN, TELEGRAM_CHATS["estadisticas"], mensaje_inicio):
        print("OK Mensaje de inicio enviado correctamente")
    else:
        print("ERROR al enviar mensaje de inicio")
    
    print()
    
    # Prueba 2: Resultado de estadísticas
    print("2. Enviando resultado de prueba a estadísticas...")
    if enviar_resultado_estadisticas("rojo", 1):
        print("OK Resultado de estadísticas enviado correctamente")
    else:
        print("ERROR al enviar resultado de estadísticas")
    
    print()
    
    # Prueba 3: Señal de racha
    print("3. Enviando señal de racha a señales...")
    if enviar_señal_rachas("azul", 3):
        print("OK Señal de racha enviada correctamente")
    else:
        print("ERROR al enviar señal de racha")
    
    print()
    
    # Prueba 4: Mensaje final
    print("4. Enviando mensaje final...")
    mensaje_final = f"<b>PRUEBA COMPLETADA</b>\n"
    mensaje_final += f"Estado: Conexión exitosa\n"
    mensaje_final += f"Hora: {datetime.now().strftime('%H:%M:%S')}\n"
    mensaje_final += f"Listo para monitoreo automático"
    
    if enviar_mensaje_telegram(TELEGRAM_TOKEN, TELEGRAM_CHATS["estadisticas"], mensaje_final):
        print("OK Mensaje final enviado correctamente")
    else:
        print("ERROR al enviar mensaje final")
    
    print()
    print("=== PRUEBA COMPLETADA ===")
    print("Si todos los mensajes se enviaron correctamente, el sistema está listo para el monitoreo automático.")

if __name__ == "__main__":
    main() 