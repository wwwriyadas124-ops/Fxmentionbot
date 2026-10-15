import os
from pyrogram import Client, filters
from pymongo import MongoClient

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
    await message.reply_text("👋 Welcome! Aapka bot successfully live ho chuka hai! 🎉")

@bot.on_message(filters.command("ping"))
async def ping_cmd(client, message):
    await message.reply_text("🏓 Pong! Bot mast chal raha hai.")

if __name__ == "__main__":
    print("Starting Telegram Bot...")
    bot.run()
