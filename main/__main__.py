import glob
from pathlib import Path
from main.utils import load_plugins
import logging
from flask import Flask
import os
import asyncio
from threading import Thread
from telethon import TelegramClient
from pyrogram import Client

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# Plugin loading
path = "main/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

# Don't be a thief 
print("Successfully deployed!")
print("By MaheshChauhan • DroneBots")

# Flask application
app = Flask(__name__)

@app.route('/')
def index():
    return "Bot is running!"

def start_telegram_bot():
    try:
        # Create a new event loop for this thread
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
        # Initialize the bot here
        API_ID = int(os.getenv("API_ID"))
        API_HASH = os.getenv("API_HASH")
        BOT_TOKEN = os.getenv("BOT_TOKEN")

        # Choose either Pyrogram or Telethon, comment out the other
        # Pyrogram example
        pyrogram_bot = Client("bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
        pyrogram_bot.start()
        print("Pyrogram bot started and running...")
        pyrogram_bot.idle()  # Keeps the bot running
        
        # Telethon example
        # telethon_bot = TelegramClient('bot', API_ID, API_HASH)
        # telethon_bot.start(bot_token=BOT_TOKEN)
        # print("Telethon bot started and running...")
        # telethon_bot.run_until_disconnected()
        
    except Exception as e:
        print(f"Error starting bot: {e}")

if __name__ == "__main__":
    # Run the bot in a separate thread
    bot_thread = Thread(target=start_telegram_bot)
    bot_thread.start()

    # Start Flask app
    port = int(os.environ.get('PORT', 10000))
    print(f"Starting Flask server on port {port}...")
    app.run(host='0.0.0.0', port=port)
