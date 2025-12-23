from pyrogram import Client, filters
from pyrogram.types import Message
from pymongo import MongoClient
import re
from BrandrdXMusic import app as Hotty

# تـوقـيـع الـسـورس
BODA_SIGNATURE = "➻ sᴏᴜʀᴄᴇ : بُودَا | ʙᴏᴅᴀ"

mongo_url_pattern = re.compile(r'mongodb(?:\+srv)?:\/\/[^\s]+')

@Hotty.on_message(filters.command("mongochk"))
async def mongo_command(client, message: Message):
    if len(message.command) < 2:
        return await message.reply("💡 **يـرجـى كـتـابـة رابـط الـمـونـجـو بـعـد الأمـر.**\nمـثـال: `/mongochk your_url`")

    mongo_url = message.command[1]
    if re.match(mongo_url_pattern, mongo_url):
        mystic = await message.reply("⚙️ **جـاري فـحـص الاتـصـال بـالـقـاعـدة..**")
        try:
            # مـحـاولـة الاتـصـال بـقـاعـدة الـبـيـانـات
            test_client = MongoClient(mongo_url, serverSelectionTimeoutMS=5000)
            test_client.server_info()  # هـيـطلـع خـطأ لـو الاتـصـال فـشـل
            await mystic.edit_text(
                f"💎 **تـم الاتـصـال بـنـجـاح، الـرابـط صـحـيـح!**\n\n{BODA_SIGNATURE}"
            )
        except Exception as e:
            await mystic.edit_text(f"❌ **فـشـل الاتـصـال بـالـقـاعـدة:**\n`{e}`")
    else:
        await message.reply(f"⚠️ **عـذراً، تـنـسـيـق الـرابـط غـيـر صـحـيـح.**\n\n{BODA_SIGNATURE}")
