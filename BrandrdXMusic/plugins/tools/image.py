import os
import shutil
from re import findall
from bing_image_downloader import downloader
from pyrogram import Client, filters
from pyrogram.types import InputMediaPhoto, Message
from BrandrdXMusic import app

# ➻ sᴏᴜʀᴄᴇ : بُودَا | ʙᴏᴅᴀ

@app.on_message(filters.command(["imgs", "صورة", "صور"], prefixes=["/", "!"]))
async def google_img_search(client: Client, message: Message):
    chat_id = message.chat.id

    try:
        query = message.text.split(None, 1)[1]
    except IndexError:
        return await message.reply("**يا ريت تكتب اسم الحاجة اللي عايز تبحث عن صورها بعد الأمر.. مثال:**\n`/صور ميسي`")

    # تحديد عدد الصور (الافتراضي 5)
    lim = findall(r"lim=\d+", query)
    try:
        lim = int(lim[0].replace("lim=", ""))
        query = query.replace(f"lim={lim}", "")
    except IndexError:
        lim = 5 

    download_dir = "downloads"

    # رسالة جاري البحث
    msg = await message.reply(f"**🔍 جاري البحث عن صور لـ: `{query}`**\n**صبرك عليا شوية..**")

    try:
        downloader.download(query, limit=lim, output_dir=download_dir, adult_filter_off=True, force_replace=False, timeout=60)
        images_dir = os.path.join(download_dir, query)
        
        if not os.path.exists(images_dir) or not os.listdir(images_dir):
            raise Exception("مفيش صور لقيتها للاسم ده.")
            
        lst = [os.path.join(images_dir, img) for img in os.listdir(images_dir)][:lim]
    except Exception as e:
        await msg.delete()
        return await message.reply(f"**حصل مشكلة وأنا بحمل الصور: {e}**")

    # تحديث العداد بشكل أشيك
    try:
        await msg.edit(f"**✅ تم العثور على {len(lst)} صور.. جاري الإرسال 🚀**")
        
        await app.send_media_group(
            chat_id=chat_id,
            media=[InputMediaPhoto(media=img) for img in lst],
            reply_to_message_id=message.id
        )
        
        # تنظيف الملفات
        shutil.rmtree(images_dir)
        await msg.delete()
        
    except Exception as e:
        if os.path.exists(images_dir):
            shutil.rmtree(images_dir)
        await msg.delete()
        return await message.reply(f"**حصل مشكلة وأنا برسل الصور للجروب: {e}**")

# ➻ sᴏᴜʀᴄᴇ : بُودَا | ʙᴏᴅᴀ
