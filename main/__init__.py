#Github.com/Vasusen-code

# from pyrogram import Client

# from telethon.sessions import StringSession
# from telethon.sync import TelegramClient

# from decouple import config
# import logging, time, sys

# logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
#                     level=logging.WARNING)

# # variables
# API_ID = config("API_ID", default=None, cast=int)
# API_HASH = config("API_HASH", default=None)
# BOT_TOKEN = config("BOT_TOKEN", default=None)
# # SESSION = config("SESSION", default=None)
# SESSION = 'BQG2W_4ArmxAlArtK8YpL6SkZ2vPcqxtmYZ76h3I9nBiS4S3hHb_6CFsEohYnQjSRe0IiTy0ZySf1IDKvRmaPrzO0wIqwATd-BoXG07_5VJB_okROL2IrgV-79aEoPRedAGBfFCErv-3YF44Uh4O9Lt1WU3rLwNfrvcKQiAK8lXUsF2UEY4gz1K4ZkhfJLofITm5BIu_AypSwKje_u9wYRoW0ZUSlBvqwS5DYtP63HyO78GbPwNs1H5omo-HNGnQsgUFhb5p2-Q3TP4Tg0Fjeg_KmGlv5d5yya97Y4jes27euP7k6qoxk1wd0MK-B-2BX1p_i54k6yxqnHpR8uq1YbX0zzZy5QAAAABBZUIQAA'
# FORCESUB = config("FORCESUB", default=None)
# AUTH = config("AUTH", default=None, cast=int)

# bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

# userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

# try:
#     userbot.start()
# except BaseException as e:
#     print(e)
#     print("Userbot Error ! Have you added SESSION while deploying?? PES456")
#     sys.exit(1)

# Bot = Client(
#     "SaveRestricted",
#     bot_token=BOT_TOKEN,
#     api_id=int(API_ID),
#     api_hash=API_HASH
# )    

# try:
#     Bot.start()
# except Exception as e:
#     print(e)
#     sys.exit(1)
