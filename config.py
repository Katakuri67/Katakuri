#(©)CodeXBotz
#Recoded By @Its_Tartaglia_Childe



import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7249806593:AAH1mumLG9OVlv6nPyoU8blog9_do5pP3tA")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "10840324"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "a630b9cf17959bcbffd661edbc719e09")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002225006101"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "5066042764"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://ganesh:8525@cluster0.gs1kks8.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")

#force sub channel id, if you want enable force sub
FORCESUB_CHANNEL = int(os.environ.get("FORCESUB_CHANNEL", "-1001642722238"))
FORCESUB_CHANNEL2 = int(os.environ.get("FORCESUB_CHANNEL2", "-1001748940647"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/53c8e8a6a14517b2a202e.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://telegra.ph/file/35137db010f6ff1e16c42.jpg")

HELP_TXT = "<b>Hi Dude!\nThis is an file to link bot work for @XANIME_UNIVERSE\n\n❏ Bot Cammands\n├/start : start the bot\n├/about : Our Information\n└/help : Help related Bot\n\n💥 Simply click on link and start the bot join both channels and try again thats it.....!\n\n🧑‍💻 Developed by <a href=https://t.me/Dumb_luffy>ʟᴜғғʏ</a></b>"

ABOUT_TXT = "<b>⟦⟧ Hi There {first}!💫\n┏━━━━━━━❪❂❫━━━━━━━━\n◈ ᴄʀᴇᴀᴛᴏʀ: <a href=https://t.me/Dumb_luffy>ʟᴜғғʏ</a>\n◈ ꜰᴏᴜɴᴅᴇʀ ᴏꜰ : <a href=https://t.me/XANIME_UNIVERSE>xᴀɴɪᴍᴇ ᴜɴɪᴠᴇʀsᴇ</a>\n◈ ᴏɴɢᴏɪɴɢ ᴄʜᴀɴɴᴇʟ : <a href=https://t.me/XANIME_ongoing>xᴀɴɪᴍᴇ ᴏɴɢᴏɪɴɢ</a>\n◈ ᴏᴜʀ ᴄᴏᴍᴍᴜɴɪᴛʏ : <a href=https://t.me/Team_Wargods>ᴛᴇᴀᴍ ᴡᴀʀɢᴏᴅs</a>\n◈ ᴀɴɪᴍᴇ ᴄʜᴀᴛ : <a href=https://t.me/xanime_chat_group>xᴀɴɪᴍᴇ ᴄʜᴀᴛ</a>\n┗━━━━━━━❪❂❫━━━━━━━━</b>"

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b>ᴘʀᴇᴘᴀʀᴇ ʏᴏᴜʀsᴇʟғ!.. {first}! 💥\n\nɪ ᴀᴍ ᴀ ꜰɪʟᴇ ꜱᴛᴏʀᴇ ʙᴏᴛ...!\nɪ ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ ᴘʀɪᴠᴀᴛᴇ ꜰɪʟᴇꜱ ᴛʜʀᴏᴜɢʜ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ʟɪɴᴋ....!\nᴘᴏᴡᴇʀᴇᴅ ʙʏ - @XANIME_UNIVERSE</b>")
try:
    ADMINS=[5205293211]
    for x in (os.environ.get("ADMINS", "5066042764").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "ʜᴇʟʟᴏ {first}!⚡\n\n🫧ᴘʟᴇᴀꜱᴇ ᴊᴏɪɴ ʙᴏᴛʜ ᴏꜰ ᴏᴜʀ ᴀɴɪᴍᴇ ᴄʜᴀɴɴᴇʟꜱ ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ...!")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "​🚫Pʟᴇᴀꜱᴇ ᴅᴏɴ'ᴛ ᴍᴇꜱꜱᴀɢᴇ ᴍᴇ ᴅɪʀᴇᴄᴛʟʏ ɪ ᴀᴍ ᴏɴʟʏ ᴡᴏʀᴋ ꜰᴏʀ​ - @XANIME_UNIVERSE"

ADMINS.append(OWNER_ID)
ADMINS.append(2058121397)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
