import os
import asyncio
from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler
from flask import Flask
from threading import Thread
from pymongo import MongoClient

# --- CLOUD SERVER KE LIYE WEB SERVER (Taaki bot 24/7 on rahe) ---
web_app = Flask(__name__)

@web_app.route('/')
def home():
    return "Bot is running 24/7 on Cloud!"

def run_web():
    web_app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

# --- BOT CONFIGURATION ---
API_ID = 33624696
API_HASH = "f405de5a5318d14c4aa6d5639708e9ff"
BOT_TOKEN = os.environ.get("BOT_TOKEN")
MONGO_URI = os.environ.get("MONGO_URI")

# --- DATABASE SETUP ---
db_client = MongoClient(MONGO_URI)
db = db_client["TelegramBot"]
users_col = db["users"]

# --- MAIN BOT APP ---
bot = Client("SessionBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@bot.on_message(filters.command("start") & filters.private)
async def start_cmd(client, message):
    text = (
        "👋 Welcome to Auto Tag & DL Bot!\n\n"
        "Abhi yeh bot development mode me hai. Aapka Cloud Server aur "
        "Database successfully connect ho chuka hai! 🎉\n\n"
        "Jald hi yahan Login ka feature add hoga."
    )
    await message.reply_text(text)

@bot.on_message(filters.command("ping"))
async def ping_cmd(client, message):
    await message.reply_text("🏓 Pong! Bot Cloud par mast chal raha hai.")

if __name__ == "__main__":
    print("Starting Web Server...")
    Thread(target=run_web).start()
    
    print("Starting Telegram Bot...")
    bot.run()
