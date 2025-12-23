import asyncio
from pyrogram import filters
from pyrogram.enums import ChatMembersFilter
from pyrogram.errors import FloodWait

from BrandrdXMusic import app
from BrandrdXMusic.misc import SUDOERS
from BrandrdXMusic.utils.database import (
    get_active_chats,
    get_authuser_names,
    get_client,
    get_served_chats,
    get_served_users,
)
from BrandrdXMusic.utils.decorators.language import language
from BrandrdXMusic.utils.formatters import alpha_to_int
from config import adminlist

# تـوقـيـع الـسـورس
BODA_SIGNATURE = "➻ sᴏᴜʀᴄᴇ : بُودَا | ʙᴏᴅᴀ"

IS_BROADCASTING = False

@app.on_message(filters.command("broadcast") & SUDOERS)
@language
async def braodcast_message(client, message, _):
    global IS_BROADCASTING
    if message.reply_to_message:
        x = message.reply_to_message.id
        y = message.chat.id
    else:
        if len(message.command) < 2:
            return await message.reply_text("❕ **يـرجـى كـتـابـة الـنـص أو الـرد عـلـى رسـالـة لـلإرسـال.**")
        query = message.text.split(None, 1)[1]
        for tag in ["-pin", "-nobot", "-pinloud", "-assistant", "-user"]:
            query = query.replace(tag, "")
        if query.strip() == "":
            return await message.reply_text("🖋 **يـرجـى تـحـديـد مـحـتـوى الإذاعـة.**")

    IS_BROADCASTING = True
    await message.reply_text("📣 **جـاري بـدء الإذاعـة الـشـامـلـة.. انـتـظـر لـحـظـة.**")

    # الإذاعـة فـي الـمـجـمـوعـات
    if "-nobot" not in message.text:
        sent = 0
        pin = 0
        chats = []
        schats = await get_served_chats()
        for chat in schats:
            chats.append(int(chat["chat_id"]))
        for i in chats:
            try:
                m = (
                    await app.forward_messages(i, y, x)
                    if message.reply_to_message
                    else await app.send_message(i, text=query)
                )
                if "-pin" in message.text:
                    try:
                        await m.pin(disable_notification=True)
                        pin += 1
                    except:
                        continue
                elif "-pinloud" in message.text:
                    try:
                        await m.pin(disable_notification=False)
                        pin += 1
                    except:
                        continue
                sent += 1
                await asyncio.sleep(0.2)
            except FloodWait as fw:
                flood_time = int(fw.value)
                if flood_time > 200:
                    continue
                await asyncio.sleep(flood_time)
            except:
                continue
        try:
            await message.reply_text(f"💎 **تـم الإرسـال إلـى {sent} مـجـمـوعـة.\n📌 تـم تـثـبـيـت {pin} رسـالـة.**")
        except:
            pass

    # الإذاعـة لـلـمـسـتـخـدمـيـن
    if "-user" in message.text:
        susr = 0
        served_users = []
        susers = await get_served_users()
        for user in susers:
            served_users.append(int(user["user_id"]))
        for i in served_users:
            try:
                m = (
                    await app.forward_messages(i, y, x)
                    if message.reply_to_message
                    else await app.send_message(i, text=query)
                )
                susr += 1
                await asyncio.sleep(0.2)
            except FloodWait as fw:
                flood_time = int(fw.value)
                if flood_time > 200:
                    continue
                await asyncio.sleep(flood_time)
            except:
                pass
        try:
            await message.reply_text(f"👤 **تـم الإرسـال إلـى {susr} مـسـتـخـدم فـي الـخـاص.**")
        except:
            pass

    # إذاعـة الـحـسـابـات الـمـسـاعـدة
    if "-assistant" in message.text:
        aw = await message.reply_text("⚙️ **جـاري الإذاعـة عـبـر الـحـسـابـات الـمـسـاعـدة..**")
        text = "📊 **تـقـريـر الـمـسـاعـد:**\n\n"
        from BrandrdXMusic.core.userbot import assistants

        for num in assistants:
            sent = 0
            client = await get_client(num)
            async for dialog in client.get_dialogs():
                try:
                    await client.forward_messages(
                        dialog.chat.id, y, x
                    ) if message.reply_to_message else await client.send_message(
                        dialog.chat.id, text=query
                    )
                    sent += 1
                    await asyncio.sleep(3)
                except FloodWait as fw:
                    flood_time = int(fw.value)
                    if flood_time > 200:
                        continue
                    await asyncio.sleep(flood_time)
                except:
                    continue
            text += f"⭐ الـمـسـاعـد {num} ➻ أرسـل لـ {sent} دردشـة.\n"
        try:
            await aw.edit_text(text + f"\n{BODA_SIGNATURE}")
        except:
            pass
    IS_BROADCASTING = False

# تـنـظـيـف الـأدمـنـيـة
async def auto_clean():
    while not await asyncio.sleep(10):
        try:
            served_chats = await get_active_chats()
            for chat_id in served_chats:
                if chat_id not in adminlist:
                    adminlist[chat_id] = []
                    async for user in app.get_chat_members(
                        chat_id, filter=ChatMembersFilter.ADMINISTRATORS
                    ):
                        if user.privileges.can_manage_video_chats:
                            adminlist[chat_id].append(user.user.id)
                    authusers = await get_authuser_names(chat_id)
                    for user in authusers:
                        user_id = await alpha_to_int(user)
                        adminlist[chat_id].append(user_id)
        except:
            continue

asyncio.create_task(auto_clean())
