import glob
from pathlib import Path
from main.utils import load_plugins
import logging
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading
# from . import bot

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

path = "main/plugins/*.py"
files = glob.glob(path)
# for name in files:
#     with open(name) as a:
#         patt = Path(a.name)
#         plugin_name = patt.stem
#         load_plugins(plugin_name.replace(".py", ""))

# Don't be a thief
print("Successfully deployed!")
print("By MaheshChauhan • DroneBots")

# Define a simple HTTP handler
class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"PES Bot is running since 2024.6.20")
        
    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

def run_http_server():
    server_address = ('', 10000)
    httpd = HTTPServer(server_address, SimpleHandler)
    print("Starting HTTP server on port 10000...")
    httpd.serve_forever()

if __name__ == "__main__":
    # Start the HTTP server in a new thread
    server_thread = threading.Thread(target=run_http_server)
    server_thread.start()

    # Start the bot in the main thread
    # bot.run_until_disconnected()
