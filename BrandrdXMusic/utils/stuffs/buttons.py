from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters, enums 

class BUTTONS(object):
    MBUTTON = [
        [
            InlineKeyboardButton("شات GPT", callback_data="mplus HELP_ChatGPT"),
            InlineKeyboardButton("السجل", callback_data="mplus HELP_History"),
            InlineKeyboardButton("ريلز", callback_data="mplus HELP_Reel")
        ],
        [
            InlineKeyboardButton("منشن الكل", callback_data="mplus HELP_TagAll"),
            InlineKeyboardButton("معلومات", callback_data="mplus HELP_Info"),
            InlineKeyboardButton("إضافات", callback_data="mplus HELP_Extra")
        ],
        [
            InlineKeyboardButton("كابلز", callback_data="mplus HELP_Couples"),
            InlineKeyboardButton("أكشن", callback_data="mplus HELP_Action"),
            InlineKeyboardButton("بحث", callback_data="mplus HELP_Search")
        ],
        [
            InlineKeyboardButton("الخطوط", callback_data="mplus HELP_Font"),
            InlineKeyboardButton("بوتات", callback_data="mplus HELP_Bots"),
            InlineKeyboardButton("تيليجراف", callback_data="mplus HELP_TG")
        ],
        [
            InlineKeyboardButton("المصدر", callback_data="mplus HELP_Source"),
            InlineKeyboardButton("صراحة / جرأة", callback_data="mplus HELP_TD"),
            InlineKeyboardButton("اختبار", callback_data="mplus HELP_Quiz")
        ],
        [
            InlineKeyboardButton("تحويل صوت", callback_data="mplus HELP_TTS"),
            InlineKeyboardButton("راديو", callback_data="mplus HELP_Radio"),
            InlineKeyboardButton("اقتباسات", callback_data="mplus HELP_Q")
        ],
        [
            InlineKeyboardButton("◁", callback_data="settings_back_helper"),
            InlineKeyboardButton("↻ رجوع ↻", callback_data="mbot_cb"),
            InlineKeyboardButton("▷", callback_data="managebot123 settings_back_helper")
        ]
    ]
