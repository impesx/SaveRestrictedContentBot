#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("API_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
BOT_TOKEN = config("BOT_TOKEN", default=None)
# SESSION = config("SESSION", default=None)
SESSION = '1BQAWZmxvcmEud2ViLnRlbGVncmFtLm9yZwG7k7zuddsheD+m+i0kgHkxKOIKR6uPEZowYX86yvmUkzl0C1wiuE3SvGrJCqrxLYJdblhXq11uTKHFl6z+dxKuXKoNYNo5//FdFlK4PpGIFKhUvo3R8dhhyHw9qgB3qH9lbMCik2ovxZCypwAFs7zg9h5O2CGToW+JxFHzB9K3x115Q5zwj1BgcDlVdOT0wUV660nrHZPYyxl4ut3jOJkEfxykF6xqGC0OtgK8dy2f1UuxgSUqpQ1ln5LSoaP/6AcVS93twvGMgV6pv6C8Xzuax5UtWczRUhrID+633vOIHu8uRc2WY+BUi5PBNr1gPD87U1NyiMFC4iSV7IC1GoKBrg=='
FORCESUB = config("FORCESUB", default=None)
AUTH = config("AUTH", default=None, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException as e:
    print(e)
    print("Userbot Error ! Have you added SESSION while deploying?? PES456")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
