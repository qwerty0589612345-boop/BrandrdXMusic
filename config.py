import re
import os
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

# تحميل المتغيرات
load_dotenv()

# ================== Telegram API ==================
API_ID = int(os.environ.get("API_ID", "0"))
API_HASH = os.environ.get("API_HASH", "")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

if not API_ID or not API_HASH or not BOT_TOKEN:
    raise SystemExit("❌ API_ID أو API_HASH أو BOT_TOKEN مش متضاف")

# ================== Database ==================
MONGO_DB_URI = os.environ.get("MONGO_DB_URI", "")

# ================== Basic Settings ==================
MUSIC_BOT_NAME = os.environ.get("MUSIC_BOT_NAME", "بُـودَا مـيوزك")
PRIVATE_BOT_MODE = os.environ.get("PRIVATE_BOT_MODE")

DURATION_LIMIT_MIN = int(os.environ.get("DURATION_LIMIT", "900"))

# ================== Logger & Owner ==================
LOGGER_ID = int(os.environ.get("LOGGER_ID", "0"))
OWNER_ID = int(os.environ.get("OWNER_ID", "7250012103"))
LOG = bool(int(os.environ.get("LOG", "1")))

# ================== Heroku (اختياري) ==================
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME")
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY")

# ================== Git ==================
UPSTREAM_REPO = os.environ.get(
    "UPSTREAM_REPO",
    "https://github.com/WCGKING/BrandrdXMusic",
)
UPSTREAM_BRANCH = os.environ.get("UPSTREAM_BRANCH", "main")
GIT_TOKEN = os.environ.get("GIT_TOKEN")

# ================== Support ==================
SUPPORT_CHANNEL = os.environ.get("SUPPORT_CHANNEL", "https://t.me/SourceBoda")
SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT", "https://t.me/music0587")

# ================== Assistant Settings ==================
AUTO_LEAVING_ASSISTANT = bool(int(os.environ.get("AUTO_LEAVING_ASSISTANT", "0")))
AUTO_GCAST = os.environ.get("AUTO_GCAST")
AUTO_GCAST_MSG = os.environ.get("AUTO_GCAST_MSG", "")

# ================== Spotify ==================
SPOTIFY_CLIENT_ID = os.environ.get(
    "SPOTIFY_CLIENT_ID",
    "bcfe26b0ebc3428882a0b5fb3e872473",
)
SPOTIFY_CLIENT_SECRET = os.environ.get(
    "SPOTIFY_CLIENT_SECRET",
    "907c6a054c214005aeae1fd752273cc4",
)

# ================== Limits ==================
SERVER_PLAYLIST_LIMIT = int(os.environ.get("SERVER_PLAYLIST_LIMIT", "50"))
PLAYLIST_FETCH_LIMIT = int(os.environ.get("PLAYLIST_FETCH_LIMIT", "25"))
SONG_DOWNLOAD_DURATION = int(os.environ.get("SONG_DOWNLOAD_DURATION_LIMIT", "180"))
SONG_DOWNLOAD_DURATION_LIMIT = int(os.environ.get("SONG_DOWNLOAD_DURATION_LIMIT", "2000"))

TG_AUDIO_FILESIZE_LIMIT = int(os.environ.get("TG_AUDIO_FILESIZE_LIMIT", "104857600"))
TG_VIDEO_FILESIZE_LIMIT = int(os.environ.get("TG_VIDEO_FILESIZE_LIMIT", "1073741824"))

# ================== Session Strings ==================
STRING1 = os.environ.get("STRING_SESSION")
STRING2 = os.environ.get("STRING_SESSION2")
STRING3 = os.environ.get("STRING_SESSION3")
STRING4 = os.environ.get("STRING_SESSION4")
STRING5 = os.environ.get("STRING_SESSION5")

# ================== Commands ==================
BANNED_USERS = filters.user()
COMMAND_PREFIXES = ["/", "!", ".", ""]

adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

# ================== Images ==================
START_IMG_URL = os.environ.get(
    "START_IMG_URL",
    "https://i.ibb.co/C3Tn6qgt/pexels-dsnsyj-1139541.jpg",
)
PING_IMG_URL = os.environ.get(
    "PING_IMG_URL",
    "https://i.ibb.co/MDCHLs5p/premium-photo-1669748157617-a3a83cc8ea23.jpg",
)
PLAYLIST_IMG_URL = "https://i.ibb.co/8QkPT67/bg2.jpg"
STATS_IMG_URL = START_IMG_URL
TELEGRAM_AUDIO_URL = PING_IMG_URL
TELEGRAM_VIDEO_URL = PLAYLIST_IMG_URL
STREAM_IMG_URL = PING_IMG_URL
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/qujhu1.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/r1lc37.jpg"
SPOTIFY_ARTIST_IMG_URL = PING_IMG_URL
SPOTIFY_ALBUM_IMG_URL = PLAYLIST_IMG_URL
SPOTIFY_PLAYLIST_IMG_URL = "https://files.catbox.moe/4st2cp.jpg"

# ================== Utils ==================
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))

DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

# ================== URL Validation ==================
if SUPPORT_CHANNEL and not re.match(r"(?:http|https)://", SUPPORT_CHANNEL):
    raise SystemExit("[ERROR] - SUPPORT_CHANNEL url غلط")

if SUPPORT_CHAT and not re.match(r"(?:http|https)://", SUPPORT_CHAT):
    raise SystemExit("[ERROR] - SUPPORT_CHAT url غلط")
