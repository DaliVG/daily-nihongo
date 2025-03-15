import os
from twilio.rest import Client
from dotenv import load_dotenv
import requests
import random
from datetime import datetime, timedelta

load_dotenv()
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
from_number = os.getenv('TWILIO_FROM_NUMBER')
to_number = os.getenv('TWILIO_TO_NUMBER')

def get_random_time():
    hour = random.randint(0, 23)
    minutes = random.randint(0, 59)
    seconds = random.randint(0, 59)
    return f"{hour:02d}:{minutes:02d}:{seconds:02d}"

def get_random_date():
    init = datetime(1990, 1, 1)
    final = datetime(2023, 12, 31)
    diference = (final - init).days
    random_days = random.randint(0, diference)
    random_date = init + timedelta(days=random_days)
    return random_date.strftime("%Y-%m-%d")


def get_random_kanji():
    url = "https://kanjiapi.dev/v1/kanji/grade-1"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

client = Client(account_sid, auth_token)

def send_message():

    kanji = random.choice(get_random_kanji())
    numero = random.randint(0, 999_999_999_999)
    random_hour = get_random_time()
    random_date = get_random_date()


    mensaje = (
        f"¡Hola! Aquí está tu práctica diaria de japonés:\n\n"
        f"Kanji: {kanji}\n"
        f"Numero: {numero}\n"
        f"hour: {random_hour}\n"
        f"Fecha: {random_date}\n\n"
        f"Intenta escribir la frase en hiragana y responde con tu intento."
    )


    message = client.messages.create(
        body=mensaje,
        from_=from_number,  
        to=to_number       
    )

    print(f"Mensaje enviado: {message.sid}")

send_message()