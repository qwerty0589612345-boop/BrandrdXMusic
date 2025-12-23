from pyrogram.enums import ParseMode

from BrandrdXMusic import app
from BrandrdXMusic.utils.database import is_on_off
from config import LOGGER_ID


async def play_logs(message, streamtype):
    if await is_on_off(2):
        logger_text = f"""
<b>{app.mention} سجل التشغيل</b>

<b>ايدي الجروب :</b> <code>{message.chat.id}</code>
<b>اسم الجروب :</b> {message.chat.title}
<b>يوزر الجروب :</b> @{message.chat.username}

<b>ايدي المستخدم :</b> <code>{message.from_user.id}</code>
<b>الاسم :</b> {message.from_user.mention}
<b>يوزر المستخدم :</b> @{message.from_user.username}

<b>الطلب :</b> {message.text.split(None, 1)[1]}
<b>نوع التشغيل :</b> {streamtype}"""
        if message.chat.id != LOGGER_ID:
            try:
                await app.send_message(
                    chat_id=LOGGER_ID,
                    text=logger_text,
                    parse_mode=ParseMode.HTML,
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
