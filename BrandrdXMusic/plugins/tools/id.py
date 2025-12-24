from BrandrdXMusic import app
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# ➻ sᴏᴜʀᴄᴇ : بُودَا | ʙᴏᴅᴀ

@app.on_message(filters.command(["id", "ايدي", "ايديه"]))
def ids(_, message):
    reply = message.reply_to_message
    if reply:
        # لو باعت الأمر ريبلاي على حد
        button = InlineKeyboardButton("✯ إغـلاق ✯", callback_data="close")
        markup = InlineKeyboardMarkup([[button]])
        message.reply_text(
            f"**👤 اسـم الـمـسـتـخـدم :** {reply.from_user.first_name}\n"
            f"**🆔 آيـدي الـمـسـتـخـدم :** `{reply.from_user.id}`",
            reply_markup=markup
        )
    else:
        # لو باعت الأمر في الجروب عادي
        button = InlineKeyboardButton("✯ إغـلاق ✯", callback_data="close")
        markup = InlineKeyboardMarkup([[button]])
        message.reply_text(
            f"**ID للمجموعة :** `{message.chat.id}`\n"
            f"**ID الخاص بك :** `{message.from_user.id}`",
            reply_markup=markup
        )

# ➻ sᴏᴜʀᴄᴇ : بُودَا | ʙᴏᴅᴀ
