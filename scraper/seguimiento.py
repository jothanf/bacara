# Módulo para el seguimiento de predicciones de mesas

import os
from datetime import datetime
import requests

class SeguimientoPredicciones:
    def __init__(self):
        # Estructura: {mesa: [ { 'prediccion': [...], 'resultados': [], 'pendiente': True, 'esperando_inicio': True } ]}
        self.seguimientos = {}
        self.log_path = 'logs/seguimiento_global.log'
        os.makedirs('logs', exist_ok=True)
        with open(self.log_path, 'a', encoding='utf-8') as f:
            f.write(f"\n--- INICIO DE SEGUIMIENTO {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ---\n")

    def log(self, mensaje):
        with open(self.log_path, 'a', encoding='utf-8') as f:
            f.write(mensaje + '\n')

    def registrar_prediccion(self, mesa, prediccion):
        if mesa not in self.seguimientos:
            self.seguimientos[mesa] = []
        self.seguimientos[mesa].append({
            'prediccion': list(prediccion),
            'resultados': [],
            'pendiente': True,
            'esperando_inicio': True  # Esperar al siguiente resultado real
        })
        self.log(f"[{datetime.now().strftime('%H:%M:%S')}] [{mesa.upper()}] NUEVA PREDICCIÓN: {', '.join(prediccion)}")

    def nuevo_resultado(self, mesa, resultado, captura_path=None):
        if mesa not in self.seguimientos:
            return
        self.log(f"[{datetime.now().strftime('%H:%M:%S')}] [{mesa.upper()}] RESULTADO: {resultado.upper()}")
        for seguimiento in self.seguimientos[mesa]:
            if not seguimiento['pendiente']:
                continue
            if seguimiento.get('esperando_inicio', False):
                # Ignorar el primer resultado tras la señal
                seguimiento['esperando_inicio'] = False
                continue
            seguimiento['resultados'].append(resultado)
            idx = len(seguimiento['resultados']) - 1
            if idx < len(seguimiento['prediccion']) and resultado == seguimiento['prediccion'][idx]:
                # WINNER
                mensaje = (f"[{datetime.now().strftime('%H:%M:%S')}] [{mesa.upper()}] WINNER: acierto en el intento {idx+1} de {len(seguimiento['prediccion'])}.\n"
                           f"  Predicción: {', '.join(seguimiento['prediccion'])}\n  Resultados: {', '.join(seguimiento['resultados'])}")
                print(mensaje)
                self.log(mensaje)
                seguimiento['pendiente'] = False
                self._enviar_telegram(mesa, seguimiento, 'WINNER', idx+1, captura_path)
            elif len(seguimiento['resultados']) == len(seguimiento['prediccion']) and seguimiento['pendiente']:
                # LOST
                mensaje = (f"[{datetime.now().strftime('%H:%M:%S')}] [{mesa.upper()}] LOST: sin aciertos en {len(seguimiento['prediccion'])} intentos.\n"
                           f"  Predicción: {', '.join(seguimiento['prediccion'])}\n  Resultados: {', '.join(seguimiento['resultados'])}")
                print(mensaje)
                self.log(mensaje)
                seguimiento['pendiente'] = False
                self._enviar_telegram(mesa, seguimiento, 'LOST', None, captura_path)

    def _enviar_telegram(self, mesa, seguimiento, tipo, intento, captura_path):
        # Configuración de tokens y chats (ajustar si es necesario)
        TELEGRAM_TOKEN_PERSONAL = "7629795944:AAEPap44tS-Ial4l2nJ4FtaRPrvBtVbTVC8"
        TELEGRAM_TOKEN_GRUPOS = "7792602918:AAFW7atIz-5qNaHVItDPv1C-hd2M679WA8s"
        TELEGRAM_CHAT_ID = "6078161114"
        TELEGRAM_CHAT_ESTADISTICAS = "-1002465111695"
        # Mensaje
        if tipo == 'WINNER':
            texto = f"<b>{mesa.upper()} - WINNER ✅</b>\n"
            texto += f"Acierto en el intento <b>{intento}</b> de {len(seguimiento['prediccion'])}\n"
        else:
            texto = f"<b>{mesa.upper()} - LOST ❌</b>\n"
            texto += f"Sin aciertos en {len(seguimiento['prediccion'])} intentos\n"
        texto += f"Predicción: {', '.join(seguimiento['prediccion'])}\n"
        texto += f"Resultados: {', '.join(seguimiento['resultados'])}\n"
        texto += f"Hora: {datetime.now().strftime('%H:%M:%S')}"
        # Enviar a ambos chats
        for token, chat in [
            (TELEGRAM_TOKEN_PERSONAL, TELEGRAM_CHAT_ID),
            (TELEGRAM_TOKEN_GRUPOS, TELEGRAM_CHAT_ESTADISTICAS)
        ]:
            try:
                url = f"https://api.telegram.org/bot{token}/sendPhoto"
                if captura_path and os.path.exists(captura_path):
                    with open(captura_path, "rb") as image:
                        files = {"photo": image}
                        data = {"chat_id": chat, "caption": texto, "parse_mode": "HTML"}
                        response = requests.post(url, files=files, data=data)
                        if response.status_code == 200:
                            print(f"[TELEGRAM] {tipo} de {mesa} enviado a chat {chat}")
                        else:
                            print(f"[TELEGRAM] Error al enviar {tipo} de {mesa} a chat {chat}: {response.status_code}")
                else:
                    print(f"[TELEGRAM] No se encontró la imagen para enviar a chat {chat}")
            except Exception as e:
                print(f"[TELEGRAM] Error enviando {tipo} de {mesa} a chat {chat}: {e}")

    def limpiar_finalizados(self):
        # Opcional: limpiar seguimientos ya terminados para ahorrar memoria
        for mesa in list(self.seguimientos.keys()):
            self.seguimientos[mesa] = [s for s in self.seguimientos[mesa] if s['pendiente']]
            if not self.seguimientos[mesa]:
                del self.seguimientos[mesa] 