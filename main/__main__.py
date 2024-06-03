import glob
from pathlib import Path
from main.utils import load_plugins
import logging
from flask import Flask
from . import bot
import os
import ntplib
from time import ctime

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# Function to sync time
def sync_time():
    try:
        client = ntplib.NTPClient()
        response = client.request('pool.ntp.org')
        if response:
            # Set system time (requires administrative privileges)
            # On Unix-based systems
            os.system(f'date -s "{ctime(response.tx_time)}"')
            print("System time synchronized.")
    except Exception as e:
        print(f"Failed to sync time: {e}")

# Sync time
sync_time()

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
    bot.run_until_disconnected()

    # Start Flask app
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
