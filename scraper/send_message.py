import requests

TOKEN = "7629795944:AAEPap44tS-Ial4l2nJ4FtaRPrvBtVbTVC8"
CHAT_ID = "6078161114"  # Reemplaza con tu chat_id real
MENSAJE = "¡Mensaje de prueba desde el bot de Python!"

# Ejemplo de sugerencia optimizada
sugerencia = ["rojo", "rojo", "rojo", "rojo", "rojo", "rojo"]
emoji = {"rojo": "🔴", "azul": "🔵"}
msg_sugerencia = " ".join([f"{i+1}{emoji[color]}" for i, color in enumerate(sugerencia)])
MENSAJE += f"\nSugerencia: {msg_sugerencia}"

# Enviar mensaje de texto
url_msg = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
params = {
    "chat_id": CHAT_ID,
    "text": MENSAJE
}
response = requests.get(url_msg, params=params)
print("Status mensaje:", response.status_code)
print("Respuesta mensaje:", response.text)

# Enviar imagen local
FILE_PATH = "capturas/mesa_resultados/mesa1/0001_mesa1_resultado_azul.png"  # Ajusta la ruta si es necesario
url_photo = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"

with open(FILE_PATH, "rb") as image:
    files = {"photo": image}
    data = {"chat_id": CHAT_ID, "caption": f"Aquí tienes tu imagen de prueba 📸\nSugerencia: {msg_sugerencia}"}
    response_photo = requests.post(url_photo, files=files, data=data)

print("Status imagen:", response_photo.status_code)
print("Respuesta imagen:", response_photo.text)
