import os
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from BrandrdXMusic import app
import requests


def upload_file(file_path):
    url = "https://catbox.moe/user/api.php"
    data = {"reqtype": "fileupload", "json": "true"}
    files = {"fileToUpload": open(file_path, "rb")}
    response = requests.post(url, data=data, files=files)

    if response.status_code == 200:
        return True, response.text.strip()
    else:
        return False, f"خطأ: {response.status_code} - {response.text}"


@app.on_message(filters.command(["tgm", "tgt", "telegraph", "tl"]))
async def get_link_group(client, message):
    if not message.reply_to_message:
        return await message.reply_text(
            "يرجى الرد على صورة أو فيديو أو ملف لرفعه على Telegraph"
        )

    media = message.reply_to_message
    file_size = 0
    if media.photo:
        file_size = media.photo.file_size
    elif media.video:
        file_size = media.video.file_size
    elif media.document:
        file_size = media.document.file_size

    if file_size > 200 * 1024 * 1024:
        return await message.reply_text(
            "حجم الملف كبير، الحد الأقصى المسموح به 200MB"
        )

    try:
        text = await message.reply("جاري المعالجة…")

        async def progress(current, total):
            try:
                await text.edit_text(
                    f"جاري التحميل… {current * 100 / total:.1f}%"
                )
            except Exception:
                pass

        try:
            local_path = await media.download(progress=progress)
            await text.edit_text("جاري الرفع على Telegraph…")

            success, upload_path = upload_file(local_path)

            if success:
                await text.edit_text(
                    f"تم رفع الملف بنجاح ✅\n\n🔗 [رابط الملف]({upload_path})\n\n➻ sᴏᴜʀᴄᴇ : بُودَا | ʙᴏᴅᴀ",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    "فتح الملف",
                                    url=upload_path,
                                )
                            ]
                        ]
                    ),
                )
            else:
                await text.edit_text(
                    f"حدث خطأ أثناء رفع الملف\n\n{upload_path}\n\n➻ sᴏᴜʀᴄᴇ : بُودَا | ʙᴏᴅᴀ"
                )

            try:
                os.remove(local_path)
            except Exception:
                pass

        except Exception as e:
            await text.edit_text(
                f"فشل رفع الملف\n\nالسبب: {e}\n\n➻ sᴏᴜʀᴄᴇ : بُودَا | ʙᴏᴅᴀ"
            )
            try:
                os.remove(local_path)
            except Exception:
                pass
            return
    except Exception:
        pass


__HELP__ = """
**أوامر رفع الملفات على Telegraph**

الأوامر المتاحة:
- `/tgm`
- `/tgt`
- `/telegraph`
- `/tl`

**طريقة الاستخدام:**
قم بالرد على صورة أو فيديو أو ملف، ثم أرسل الأمر.

**ملاحظة:**
يجب أن يكون حجم الملف أقل من 200MB.

➻ sᴏᴜʀᴄᴇ : بُودَا | ʙᴏᴅᴀ
"""

__MODULE__ = "Tᴇʟᴇɢʀᴀᴘʜ"
