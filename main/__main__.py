import glob
from pathlib import Path
from main.utils import load_plugins
import logging
from flask import Flask
from . import bot
import os

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

if __name__ == "__main__":
    # Start the bot
    from threading import Thread

    def start_bot():
        bot.run_until_disconnected()

    # Run the bot in a separate thread
    Thread(target=start_bot).start()

    # Start Flask app
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
