import glob
from pathlib import Path
from main.utils import load_plugins
import logging
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading
from . import bot

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

path = "main/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

#Don't be a thief 
print("Successfully deployed!")
print("By MaheshChauhan • DroneBots")

# Define a simple HTTP handler
class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Bot is running")

def run_http_server():
    server_address = ('', 10000)
    httpd = HTTPServer(server_address, SimpleHandler)
    print("Starting HTTP server on port 10000...")
    httpd.serve_forever()

def start_bot():
    bot.run_until_disconnected()

if __name__ == "__main__":
    # Start the bot in a new thread
    bot_thread = threading.Thread(target=start_bot)
    bot_thread.start()

    # Start the HTTP server
    run_http_server()
