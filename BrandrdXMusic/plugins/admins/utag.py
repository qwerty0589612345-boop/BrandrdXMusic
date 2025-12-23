import asyncio
import random
from pyrogram import Client, filters
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.errors import UserNotParticipant
from pyrogram.types import ChatPermissions
from BrandrdXMusic import app
from BrandrdXMusic.utils.branded_ban import admin_filter

SPAM_CHATS = {}


@app.on_message(
    filters.command(["utag", "منشن_مستمر", "نادي_الكل"], prefixes=["/", "@", ".", "#"]) & admin_filter
)
async def tag_all_users(_, message):
    global SPAM_CHATS
    chat_id = message.chat.id
    
    # التأكد إن المستخدم كتب نص المنشن
    if len(message.text.split()) == 1:
        await message.reply_text(
            "**يا حب اكتب أي حاجة بعد الأمر عشان أنادي للكل، مثلاً:**\n`/utag صحصحوا معايا`"
        )
        return

    text = message.text.split(None, 1)[1]
    
    # رسالة البداية
    await message.reply_text(
        "**✅ المنشن المستمر بدأ بنجاح يا وحش!**\n\n"
        "**⏳ بنادي للناس كل 7 ثواني عشان الحظر.**\n\n"
        "**🚫 لو عايز توقف استخدم الأمر » /stoputag**"
    )

    SPAM_CHATS[chat_id] = True
    f = True
    
    while f:
        # فحص لو العملية وقفت
        if SPAM_CHATS.get(chat_id) == False:
            await message.reply_text("**تم إيقاف المنشن المستمر بنجاح. ✅**\n\nּبـٰﯡدَا ׀ 𝗦𝗢𝗨𝗥𝗖𝗘 𝗕𝗢𝗗𝗔 👣")
            break
            
        usernum = 0
        usertxt = ""
        
        try:
            async for m in app.get_chat_members(message.chat.id):
                # فحص لو تم الإيقاف أثناء جلب الأعضاء
                if SPAM_CHATS.get(chat_id) == False:
                    break
                    
                if m.user.is_bot:
                    continue
                    
                usernum += 1
                usertxt += f"\n⊚ [{m.user.first_name}](tg://user?id={m.user.id})\n"
                
                # منشن لـ 5 أعضاء في المرة الواحدة
                if usernum == 5:
                    await app.send_message(
                        message.chat.id,
                        f"**{text}**\n{usertxt}\n\n"
                        f"**➥ الإيقاف بواسطة » /stoputag**\n\n"
                        f"**ּبـٰﯡدَا ׀ 𝗦𝗢𝗨𝗥𝗖𝗘 𝗕𝗢𝗗𝗔 👣**",
                    )
                    usernum = 0
                    usertxt = ""
                    await asyncio.sleep(7) # وقت الانتظار لتجنب الفلود
                    
        except Exception as e:
            print(f"Error in utag: {e}")
            break


@app.on_message(
    filters.command(
        ["stoputag", "stopuall", "وقف_المنشن", "ايقاف"],
        prefixes=["/", ".", "@", "#"],
    )
    & admin_filter
)
async def stop_tagging(_, message):
    global SPAM_CHATS
    chat_id = message.chat.id
    
    if SPAM_CHATS.get(chat_id) == True:
        SPAM_CHATS[chat_id] = False
        return await message.reply_text("**ثواني وبوقف المنشن المستمر عشانك يا غالي... ⏳**")
    else:
        await message.reply_text("**يا فنان مفيش عملية منشن شغالة دلوقتي أصلاً. ❌**")
