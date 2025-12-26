import time
import asyncio
from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from youtubesearchpython.__future__ import VideosSearch

import config
from BrandrdXMusic import app
from BrandrdXMusic.misc import _boot_
from BrandrdXMusic.plugins.sudo.sudoers import sudoers_list
from BrandrdXMusic.utils.database import (
    add_served_chat,
    add_served_user,
    blacklisted_chats,
    get_lang,
    is_banned_user,
    is_on_off,
)
from BrandrdXMusic.utils.decorators.language import LanguageStart
from BrandrdXMusic.utils.formatters import get_readable_time
from BrandrdXMusic.utils.inline import help_pannel, private_panel, start_panel
from config import BANNED_USERS
from strings import get_string

# ➻ sᴏᴜʀᴄᴇ : بُودَا | ʙᴏᴅَا

@app.on_message(filters.command(["start"]) & filters.private & ~BANNED_USERS)
@LanguageStart
async def start_pm(client, message: Message, _):
    await add_served_user(message.from_user.id)
    await message.react("❤")
    if len(message.text.split()) > 1:
        name = message.text.split(None, 1)[1]
        if name[0:4] == "help":
            keyboard = help_pannel(_)
            await message.reply_sticker("CAACAgUAAxkBAAEQI1RlTLnRAy4h9lOS6jgS5FYsQoruOAAC1gMAAg6ryVcldUr_lhPexzME")
            return await message.reply_photo(
                photo="https://files.catbox.moe/pghxm8.jpg",
                caption=_["help_1"].format(config.SUPPORT_CHAT),
                reply_markup=keyboard,
            )
        if name[0:3] == "sud":
            await sudoers_list(client=client, message=message, _=_)
            if await is_on_off(2):
                return await app.send_message(
                    chat_id=config.LOGGER_ID,
                    text=f"**المستخدم {message.from_user.mention} فتح البوت عشان يشوف قائمة المطورين.**\n\n**الأيدي :** `{message.from_user.id}`\n**اليوزر :** @{message.from_user.username}",
                )
            return
        if name[0:3] == "inf":
            m = await message.reply_text("🔎")
            query = (str(name)).replace("info_", "", 1)
            query = f"https://www.youtube.com/watch?v={query}"
            results = VideosSearch(query, limit=1)
            for result in (await results.next())["result"]:
                title = result["title"]
                duration = result["duration"]
                views = result["viewCount"]["short"]
                thumbnail = result["thumbnails"][0]["url"].split("?")[0]
                channellink = result["channel"]["link"]
                channel = result["channel"]["name"]
                link = result["link"]
                published = result["publishedTime"]
            searched_text = _["start_6"].format(
                title, duration, views, published, channellink, channel, app.mention
            )
            key = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text=_["S_B_8"], url=link),
                        InlineKeyboardButton(text=_["S_B_9"], url=config.SUPPORT_CHAT),
                    ],
                ]
            )
            await m.delete()
            await app.send_photo(
                chat_id=message.chat.id,
                photo=thumbnail,
                caption=searched_text,
                reply_markup=key,
            )
            if await is_on_off(2):
                return await app.send_message(
                    chat_id=config.LOGGER_ID,
                    text=f"**المستخدم {message.from_user.mention} فتح البوت عشان يشوف معلومات المسار.**\n\n**الأيدي :** `{message.from_user.id}`\n**اليوزر :** @{message.from_user.username}",
                )
    else:

        try:
            out = private_panel(_)
            # ترحيب معرب
            lol = await message.reply_text("✨ منور يا {}.. ❣️".format(message.from_user.mention))
            await lol.edit_text("✨ أهلاً بك {}.. 🥳".format(message.from_user.mention))
            await lol.edit_text("✨ نورت البوت يا حب {}.. 💥".format(message.from_user.mention))
            await lol.edit_text("✨ مستني إيه؟ شغل دلوقتي {}.. 🤩".format(message.from_user.mention))
            await lol.edit_text("✨ البوت بوتك يا قلبي {}.. 💌".format(message.from_user.mention))
            await lol.edit_text("✨ استمتع بالأغاني مع {}.. 💞".format(message.from_user.mention))
               
            await lol.delete()
            lols = await message.reply_text("**⚡ ج**")
            await asyncio.sleep(0.1)
            await lols.edit_text("**⚡ جا**")        
            await asyncio.sleep(0.1)
            await lols.edit_text("**⚡ جارِ**")
            await asyncio.sleep(0.1)
            await lols.edit_text("**⚡ جاري الـ**")
            await asyncio.sleep(0.1)
            await lols.edit_text("**⚡ جاري التحـ**")
            await asyncio.sleep(0.1)
            await lols.edit_text("**⚡ جاري التحميل**")
            await asyncio.sleep(0.1)
            await lols.edit_text("**⚡ جاري التحميل..**")
            await asyncio.sleep(0.1)
            await lols.edit_text("**⚡ جاري التحميل...**")
            await asyncio.sleep(0.1)
            await lols.edit_text("**⚡ جاري التحميل....**")

            m = await message.reply_sticker("CAACAgUAAxkBAAEQI1BlTLmx7PtOO3aPNshEU2gCy7iAFgACNQUAApqMuVeA6eJ50VbvmDME")
            
            # محاولة جلب صورة المستخدم
            if message.from_user.photo:
                userss_photo = await app.download_media(
                    message.from_user.photo.big_file_id,
                )
            else:
                userss_photo = "https://files.catbox.moe/pghxm8.jpg"
            
            chat_photo = userss_photo if userss_photo else "https://files.catbox.moe/pghxm8.jpg"

        except Exception:
            chat_photo = "https://files.catbox.moe/pghxm8.jpg"
            
        await lols.delete()
        await m.delete()
        await message.reply_photo(
            photo=chat_photo,
            caption=_["start_2"].format(message.from_user.mention, app.mention) + "\n\n➻ sᴏᴜʀᴄᴇ : بُودَا | ʙᴏᴅَا",
            reply_markup=InlineKeyboardMarkup(out),
        )
        if await is_on_off(config.LOG):
            sender_id = message.from_user.id
            sender_name = message.from_user.first_name
            return await app.send_message(
                config.LOG_GROUP_ID,
                f"**{message.from_user.mention} بدأ تشغيل البوت الآن.**\n\n**الأيدي :** `{sender_id}`\n**الاسم :** {sender_name}",
            )          

@app.on_message(filters.command(["start"]) & filters.group & ~BANNED_USERS)
@LanguageStart
async def start_gp(client, message: Message, _):
    out = start_panel(_)
    uptime = int(time.time() - _boot_)
    await message.reply_photo(
        photo="https://files.catbox.moe/pghxm8.jpg",
        caption=_["start_1"].format(app.mention, get_readable_time(uptime)) + "\n\n➻ sᴏᴜʀᴄᴇ : بُودَا | ʙᴏᴅَا",
        reply_markup=InlineKeyboardMarkup(out),
    )
    return await add_served_chat(message.chat.id)

@app.on_message(filters.new_chat_members, group=-1)
async def welcome(client, message: Message):
    for member in message.new_chat_members:
        try:
            language = await get_lang(message.chat.id)
            _ = get_string(language)
            if await is_banned_user(member.id):
                try:
                    await message.chat.ban_member(member.id)
                except:
                    pass
            if member.id == app.id:
                if message.chat.type != ChatType.SUPERGROUP:
                    await message.reply_text(_["start_4"])
                    return await app.leave_chat(message.chat.id)
                
                out = start_panel(_)
                await message.reply_photo(
                    photo="https://files.catbox.moe/pghxm8.jpg",
                    caption=_["start_3"].format(
                        message.from_user.first_name,
                        app.mention,
                        message.chat.title,
                        app.mention,
                    ) + "\n\n➻ sᴏᴜʀᴄᴇ : بُودَا | ʙᴏᴅَا",
                    reply_markup=InlineKeyboardMarkup(out),
                )
                await add_served_chat(message.chat.id)
                await message.stop_propagation()
        except Exception:
            pass

# ➻ sᴏᴜʀᴄᴇ : بُودَا | ʙᴏᴅَا
