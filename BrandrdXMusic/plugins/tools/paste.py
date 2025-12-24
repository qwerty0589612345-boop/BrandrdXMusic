import asyncio
import os
import re

import aiofiles
from pykeyboard import InlineKeyboard
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton

from aiohttp import ClientSession
from BrandrdXMusic import app
from BrandrdXMusic.utils.errors import capture_err
from BrandrdXMusic.utils.pastebin import HottyBin

# ➻ sᴏᴜʀᴄᴇ : بُودَا | ʙᴏᴅَا

pattern = re.compile(r"^text/|json$|yaml$|xml$|toml$|x-sh$|x-shellscript$")

@app.on_message(filters.command(["paste", "رفع", "باست"]))
@capture_err
async def paste_func(_, message):
    if not message.reply_to_message:
        return await message.reply_text("**يـا حـبـيـب قـلـبـي رد عـلـى الـنـص أو الـمـلـف بـأمـر الـرفـع.. 🔗**")
    
    m = await message.reply_text("**جـاري الـرفـع الـآن.. صـبـرك يـا رايـق.. ⏳**")
    
    if message.reply_to_message.text:
        content = str(message.reply_to_message.text)
    elif message.reply_to_message.document:
        document = message.reply_to_message.document
        if document.file_size > 1048576:
            return await m.edit("**يـا بـطـل الـمـلـف كـبـيـر أوي.. لازم يـكـون أقـل مـن 1 مـيـجـا.. ❌**")
        if not pattern.search(document.mime_type):
            return await m.edit("**مـقـدرش أرفـع غـيـر الـمـلـفـات الـنـصـيـة بـس.. 📑**")
        
        doc = await message.reply_to_message.download()
        async with aiofiles.open(doc, mode="r") as f:
            content = await f.read()
        os.remove(doc)
    
    link = await HottyBin(content)
    button = InlineKeyboard(row_width=1)
    button.add(InlineKeyboardButton(text="✧ رابـط الـنـص الـمـرفـوع ✧", url=link))

    await m.delete()
    try:
        await message.reply(
            f"**تـم الـرفـع بـنـجـاح يـا رايـق.. ✨**\n\n**➻ sᴏᴜʀᴄᴇ : بُودَا | ʙᴏᴅَا**", 
            quote=False, 
            reply_markup=button
        )
        
    except Exception:
        pass

# ➻ sᴏᴜʀᴄᴇ : بُودَا | ʙᴏᴅَا
