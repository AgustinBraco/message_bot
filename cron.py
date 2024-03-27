# Importar dependencias:
import schedule
import time
import os
from dotenv import load_dotenv
from rocket import send_message

# Configuracion de mensajes:
CHAT = 'Agustin Braco'

WELCOME = "Donatellbot :turtle: les desea una buena semana."

DAILY = """@here
It's daily time! :turtle: 
https://meet.google.com/oco-csqg-kbk"""

WEEKLY = """@here
It's weekly time! :turtle: 
https://meet.google.com/oco-csqg-kbk"""

KT = """@here
It's mini-kt time! :turtle: 
https://meet.google.com/oco-csqg-kbk"""

WEEKEND = "Donatellbot :turtle: les desea un buen finde."

# Acceder a las variables de entorno:
load_dotenv()
NAME = os.environ.get("NAME")
PASSWORD = os.environ.get("PASSWORD")

# Funciones a ejecutar:
def send_welcome_message():
    send_message(NAME, PASSWORD, CHAT, WELCOME)

def send_daily_meeting():
    send_message(NAME, PASSWORD, CHAT, DAILY)

def send_weekly_meeting():
    send_message(NAME, PASSWORD, CHAT, WEEKLY)

def send_kt_meeting():
    send_message(NAME, PASSWORD, CHAT, KT)

def send_weekend_message():
    send_message(NAME, PASSWORD, CHAT, WEEKEND)

# Cron listener:
schedule.every().monday.at("08:00").do(send_welcome_message)
schedule.every().monday.at("10:00").do(send_daily_meeting)
schedule.every().tuesday.at("10:00").do(send_daily_meeting)
schedule.every().wednesday.at("10:00").do(send_weekly_meeting)
schedule.every().thursday.at("10:00").do(send_daily_meeting)
schedule.every().friday.at("10:00").do(send_daily_meeting)
schedule.every().friday.at("14:00").do(send_kt_meeting)
schedule.every().friday.at("18:00").do(send_weekend_message)

# Prender cron:
while True:
    schedule.run_pending()
    time.sleep(1)