import asyncio
from pyrogram import enums, filters
from pyrogram.errors import FloodWait
from BrandrdXMusic import app

# ➻ sᴏᴜʀᴄᴇ : بُودَا | ʙᴏᴅᴀ

@app.on_message(filters.command(["bots", "البوتات"]) & filters.group)
async def bots(client, message):
    try:
        # رسالة انتظار خفيفة
        mystic = await message.reply_text("**جاري جلب قائمة البوتات.. استنى ثواني 🔍**")
        
        botList = []
        async for bot in app.get_chat_members(
            message.chat.id, filter=enums.ChatMembersFilter.BOTS
        ):
            botList.append(bot.user)
        
        lenBotList = len(botList)
        if lenBotList == 0:
            return await mystic.edit("**مفيش بوتات في المجموعة دي غيري يا حُب! 🤖**")

        text3 = f"**🤖 قائمة البوتات - {message.chat.title}**\n\n"
        
        while len(botList) > 1:
            bot = botList.pop(0)
            text3 += f"│ ├ @{bot.username}\n"
        else:
            bot = botList.pop(0)
            text3 += f"│ └ @{bot.username}\n\n"
            text3 += f"**✅ إجمالي عدد البوتات**: {lenBotList}"
            
        await mystic.edit(text3)
        
    except FloodWait as e:
        await asyncio.sleep(e.value)
    except Exception as e:
        await message.reply_text(f"**حصل مشكلة وأنا بجيب القائمة: {e}**")

# ➻ sᴏᴜʀᴄᴇ : بُودَا | ʙᴏᴅᴀ
