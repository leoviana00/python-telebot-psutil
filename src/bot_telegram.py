import psutil
import telebot
from functions import *
from credentials import *


bot = telebot.TeleBot(telegram_token )

# ---------------------------
#           CPU
# ---------------------------

# Uso da CPU como porcentagem
@bot.message_handler(commands=["cpu_carga"])
def uso_cpu(mensagem):
    bot.send_message(mensagem.chat.id, 'A carga da CPU do sistema é {} %' . format ( get_cpu_usage_pct ()))

# Frequência da CPU
@bot.message_handler(commands=["cpu_freq"])
def uso_cpu(mensagem):
    bot.send_message(mensagem.chat.id, 'Frequência da CPU é {} MHz' . format ( get_cpu_frequency ()))

# Temperatura da CPU
@bot.message_handler(commands=["cpu_temp"])
def uso_cpu(mensagem):
    bot.send_message(mensagem.chat.id, 'CPU temperature is {} degC' . format ( get_cpu_temp ()))

# ---------------------------
#          MEMÓRIA
# ---------------------------


# ---------------------------
#           SWAP
# ---------------------------



def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
    Escolha uma opção para continuar (Clique no item):
    /cpu_carga Verificar uso da CPU como porcentagem
    /cpu_freq Verificar frequência da CPU
    /cpu_temp Verificar temperatura da CPU
    Responder qualquer outra coisa não vai funcionar, clique em uma das opções
    """
    bot.reply_to(mensagem, texto)

bot.polling()