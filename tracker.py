import time
import pickle
import telebot
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from flask import Flask
import os

bot_token = os.getenv("BOT_TOKEN")
user_id = int(os.getenv("USER_ID"))
targets = os.getenv("TARGETS").split(',')

bot = telebot.TeleBot(bot_token)
app = Flask(__name__)

@app.route('/')
def home():
    return "Tracker is running!"

def send(message):
    try:
        bot.send_message(user_id, message)
    except Exception as e:
        print("Telegram Error:", e)

options = uc.ChromeOptions()
driver = uc.Chrome(options=options)
driver.get("https://web.whatsapp.com")

import base64

# Load cookies from base64 file
with open("cookies.b64", "rb") as f:
    b64data = f.read()
cookies = pickle.loads(base64.b64decode(b64data))
for cookie in cookies:
    driver.add_cookie(cookie)
driver.refresh()

print("✅ Tracker Started!")
send("✅ Tracker Started Successfully!")

last_status = {}

while True:
    try:
        for number in targets:
            driver.get(f"https://web.whatsapp.com/send?phone={number}")
            time.sleep(5)
            try:
                status = driver.find_element(By.XPATH, "//span[@title='online']").text
                if last_status.get(number) != status:
                    send(f"📱 {number} is ONLINE")
                    last_status[number] = status
            except:
                if last_status.get(number) != "offline":
                    send(f"📴 {number} is OFFLINE")
                    last_status[number] = "offline"
        time.sleep(15)
    except Exception as e:
        print("Error:", e)
        time.sleep(30)
