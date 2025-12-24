import random
from pyrogram import Client
from pyrogram.types import Message
from pyrogram import filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InputMediaPhoto,
    InputMediaVideo,
    Message,
)
from config import LOGGER_ID as LOG_GROUP_ID
from BrandrdXMusic import app
from BrandrdXMusic.utils.database import get_assistant
from BrandrdXMusic.utils.database import delete_served_chat

# ➻ sᴏᴜʀᴄᴇ : بُودَا | ʙᴏᴅَا

photo = [
    "https://files.catbox.moe/ht74e3.jpg",
    "https://files.catbox.moe/4st2cp.jpg",
    "https://files.catbox.moe/r1lc37.jpg",
    "https://files.catbox.moe/qujhu1.jpg",
    "https://files.catbox.moe/efzuds.jpg",
]


@app.on_message(filters.left_chat_member)
async def on_left_chat_member(_, message: Message):
    try:
        userbot = await get_assistant(message.chat.id)

        left_chat_member = message.left_chat_member
        if left_chat_member and left_chat_member.id == (await app.get_me()).id:
            remove_by = (
                message.from_user.mention if message.from_user else "مـسـتـخـدم غـيـر مـعـروف"
            )
            title = message.chat.title
            username = (
                f"@{message.chat.username}" if message.chat.username else "مـجـمـوعـة خـاصـة"
            )
            chat_id = message.chat.id
            left = f"✫ <b><u>#تـم_الـطـرد_مـن_الـمـجـمـوعـة</u></b> ✫\n\n**اسـم الـمـجـمـوعـة :** {title}\n\n**آيـدي الـمـجـمـوعـة :** `{chat_id}`\n\n**بـواسـطـة :** {remove_by}\n\n**الـبـوت :** @{app.username}"
            await app.send_photo(LOG_GROUP_ID, photo=random.choice(photo), caption=left)
            await delete_served_chat(chat_id)
            await userbot.leave_chat(chat_id)
    except Exception as e:
        return

# ➻ sᴏᴜʀᴄᴇ : بُودَا | ʙᴏᴅَا
