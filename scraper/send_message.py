import requests

# Token del bot de Telegram
TOKEN = "7792602918:AAFW7atIz-5qNaHVItDPv1C-hd2M679WA8s"

# Configuración de mensajes por chat ID
mensajes_config = [
    {
        "chat_id": "-1002465111695",
        "mensaje": "estadisticas",
        "descripcion": "Chat Estadísticas"
    },
    {
        "chat_id": "-1002539477075", 
        "mensaje": "señales",
        "descripcion": "Chat Señales"
    }
]

def enviar_mensaje(token, chat_id, mensaje):
    url_msg = f"https://api.telegram.org/bot{token}/sendMessage"
    params = {
        "chat_id": chat_id,
        "text": mensaje
    }
    response = requests.get(url_msg, params=params)
    print(f"Status mensaje ({chat_id}):", response.status_code)
    print("Respuesta mensaje:", response.text)

# Enviar mensajes a cada chat ID
for config in mensajes_config:
    print(f"\nEnviando a: {config['descripcion']} (chat_id: {config['chat_id']})")
    enviar_mensaje(TOKEN, config["chat_id"], config["mensaje"])
