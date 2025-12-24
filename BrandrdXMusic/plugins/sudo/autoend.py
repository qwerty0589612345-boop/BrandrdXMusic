from pyrogram import filters
from pyrogram.types import Message

from BrandrdXMusic import app
from BrandrdXMusic.misc import SUDOERS
from BrandrdXMusic.utils.database import autoend_off, autoend_on

# ➻ sᴏᴜʀᴄᴇ : بُودَا | ʙᴏᴅَا

@app.on_message(filters.command(["autoend", "الإنهاء_التلقائي"]) & SUDOERS)
async def auto_end_stream(_, message: Message):
    usage = "**الـاسـتـخـدام :**\n\n/autoend [تـفـعـيـل | تـعـطـيـل]"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    
    state = message.text.split(None, 1)[1].strip().lower()
    
    if state in ["enable", "تـفـعـيـل"]:
        await autoend_on()
        await message.reply_text(
            "**تـم تـفـعـيـل الـإنـهـاء الـتـلـقـائـي بـنـجـاح.. ✨**\n\n**سـيـقـوم الـمـسـاعـد بـمـغـادره الـمـكـالـمـة تـلـقـائـيـاً عـنـد خـروج الـأعـضـاء.**"
        )
    elif state in ["disable", "تـعـطـيـل"]:
        await autoend_off()
        await message.reply_text("**تـم تـع_طـيـل الـإنـهـاء الـتـلـقـائـي بـنـجـاح.. ✨**")
    else:
        await message.reply_text(usage)

# ➻ sᴏᴜʀᴄᴇ : بُودَا | ʙᴏᴅَا
