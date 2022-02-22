import psutil
import telebot
from src.funcoes import *
# from credentials import *
from colorama import init, Fore, Style
init()
import yaml

telegramIntegration = False
try:
    stream = open("config/telegram.yaml", 'r', encoding='utf8')
    streamConfigTelegram = yaml.safe_load(stream)
    telegramIntegration = streamConfigTelegram['telegram_enable']
    telegramChatId = streamConfigTelegram['chat_ids']
    telegramBotToken = streamConfigTelegram['botfather_token']
except FileNotFoundError:
    print('Info: Telegram not configure, rename EXAMPLE-telegram.yaml to telegram.yaml')
    heroesClickedTelegram = True
except KeyError:
    print(Fore.RED +'Error: Please update the telegram.yaml file. \nErro: Por favor atualize o arquivo telegram.yaml', Style.RESET_ALL)
    exit()

bot = telebot.TeleBot(telegramBotToken)

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

# Saída do uso atual da RAM em MB
@bot.message_handler(commands=["mem_uso"])
def uso_cpu(mensagem):
    bot.send_message(mensagem.chat.id, 'Uso de RAM é {} MB' . format ( int ( get_ram_usage () / 1024 / 1024 ))) 


# Saída total de RAM em MB
@bot.message_handler(commands=["mem_total"])
def uso_cpu(mensagem):
    bot.send_message(mensagem.chat.id, 'RAM total é {} MB' . format ( int ( get_ram_total () / 1024 / 1024 )))


# Exibe o uso atual de RAM como uma porcentagem.
@bot.message_handler(commands=["mem_uso_pct"])
def uso_cpu(mensagem):
    bot.send_message(mensagem.chat.id, 'Uso de RAM é {} %' . format ( get_ram_usage_pct ()))

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
    /mem_uso Verificar uso atual da RAM em MB
    /mem_total Verificar RAM total
    /mem_uso_pct Verificar Uso de RAM em porcentagem
    Responder qualquer outra coisa não vai funcionar, clique em uma das opções
    """
    bot.reply_to(mensagem, texto)

bot.polling()