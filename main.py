import os
import asyncio
from fastapi import FastAPI
from pyrogram import Client, filters
from pymongo import MongoClient
import uvicorn

# --- FASTAPI WEB SERVER (Render ke liye) ---
app = FastAPI()

@app.get("/")
def home():
    return {"status": "Bot is running 24/7 on Cloud!"}

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
        "Aapka Cloud Server aur Database successfully connect ho chuka hai! 🎉\n\n"
    )
    await message.reply_text(text)

@bot.on_message(filters.command("ping"))
async def ping_cmd(client, message):
    await message.reply_text("🏓 Pong! Bot Cloud par mast chal raha hai.")

# --- STARTUP EVENT (Web server ke sath bot ko chalu karna) ---
@app.on_event("startup")
async def startup_event():
    print("Starting Telegram Bot...")
    await bot.start()
    print("🚀 Bot is 100% Online and Live!")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
