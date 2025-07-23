import subprocess
from telegram.ext import Updater, CommandHandler

# Pega aquí el token de tu bot de Telegram
TELEGRAM_TOKEN = 'AQUI_TU_TOKEN'
# Opcional: pon tu user_id para restringir el control
AUTHORIZED_USER_ID = 123456789  # Cambia esto por tu ID real

# Ruta al main.py (ajusta si es necesario)
MAIN_PY = 'main.py'

# Función para verificar autorización
def is_authorized(update):
    return update.effective_user.id == AUTHORIZED_USER_ID

# Comando /start
def start_command(update, context):
    if not is_authorized(update):
        update.message.reply_text('No autorizado.')
        return
    try:
        subprocess.run(['python3', MAIN_PY, 'start'])
        update.message.reply_text('Servidor iniciado.')
    except Exception as e:
        update.message.reply_text(f'Error al iniciar: {e}')

# Comando /stop
def stop_command(update, context):
    if not is_authorized(update):
        update.message.reply_text('No autorizado.')
        return
    try:
        subprocess.run(['python3', MAIN_PY, 'stop'])
        update.message.reply_text('Servidor detenido.')
    except Exception as e:
        update.message.reply_text(f'Error al detener: {e}')

# Comando /status (opcional)
def status_command(update, context):
    if not is_authorized(update):
        update.message.reply_text('No autorizado.')
        return
    try:
        result = subprocess.run(['python3', MAIN_PY], capture_output=True, text=True)
        update.message.reply_text(f'Status:
{result.stdout}')
    except Exception as e:
        update.message.reply_text(f'Error al consultar status: {e}')

def main():
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start_command))
    dp.add_handler(CommandHandler('stop', stop_command))
    dp.add_handler(CommandHandler('status', status_command))
    updater.start_polling()
    print('Bot de control iniciado. Esperando comandos...')
    updater.idle()

if __name__ == '__main__':
    main() 