import asyncio
import logging

from pyrogram import filters
from pyrogram.enums import ChatMemberStatus
from pyrogram.errors import (
    ChatAdminRequired,
    InviteRequestSent,
    UserAlreadyParticipant,
    UserNotParticipant,
)
from pyrogram.types import Message

from config import BANNED_USERS, adminlist
from strings import get_string
from BrandrdXMusic import app
from BrandrdXMusic.misc import SUDOERS
from BrandrdXMusic.utils.database import (
    get_assistant,
    get_cmode,
    get_lang,
    get_playmode,
    get_playtype,
)
from BrandrdXMusic.utils.logger import play_logs
from BrandrdXMusic.utils.stream.stream import stream


RADIO_STATION = {
    "Air Bilaspur": "http://air.pc.cdn.bitgravity.com/air/live/pbaudio110/playlist.m3u8",
    "Air Raipur": "http://air.pc.cdn.bitgravity.com/air/live/pbaudio118/playlist.m3u8",
    "Capital FM": "http://media-ice.musicradio.com/CapitalMP3?.mp3&listening-from-radio-garden=1616312105154",
    "English": "https://hls-01-regions.emgsound.ru/11_msk/playlist.m3u8",
    "Mirchi": "http://peridot.streamguys.com:7150/Mirchi",
    "Radio Today": "http://stream.zenolive.com/8wv4d8g4344tv",

    # 🕌 إذاعة القرآن الكريم
    "قرآن كريم": "https://stream.radiojar.com/8s5u5tpdtwzuv",

    "YouTube": "https://www.youtube.com/live/eu191hR_LEc?si=T-9QYD548jd0Mogp",
    "Zee News": "https://www.youtube.com/live/TPcmrPrygDc?si=hiHBkIidgurQAd1P",
    "Aaj Tak": "https://www.youtube.com/live/Nq2wYlWFucg?si=usY4UYiSBInKA0S1",
}

valid_stations = "\n".join([f"`{name}`" for name in sorted(RADIO_STATION.keys())])


@app.on_message(
    filters.command(["radioplayforce", "radio", "cradio"])
    & filters.group
    & ~BANNED_USERS
)
async def radio(client, message: Message):
    msg = await message.reply_text("**يرجى الانتظار قليلاً جاري التحضير.. ✨**")
    try:
        try:
            userbot = await get_assistant(message.chat.id)
            get = await app.get_chat_member(message.chat.id, userbot.id)
        except ChatAdminRequired:
            return await msg.edit_text(
                f"**عذراً، لا أملك صلاحية إضافة المساعد {userbot.mention} إلى المجموعة.. 🥀**"
            )
        if get.status == ChatMemberStatus.BANNED:
            return await msg.edit_text(
                text=f"**الحساب المساعد {userbot.mention} محظور في هذه المجموعة {message.chat.title} ❌**\n\n𖢵 ɪᴅ : `{userbot.id}`\n𖢵 ɴᴀᴍᴇ : {userbot.mention}\n𖢵 ᴜsᴇʀɴᴀᴍᴇ : @{userbot.username}\n\n**يرجى إلغاء الحظر عنه والمحاولة مرة أخرى.. ✨**",
            )
    except UserNotParticipant:
        if message.chat.username:
            invitelink = message.chat.username
            try:
                await userbot.resolve_peer(invitelink)
            except Exception as ex:
                logging.exception(ex)
        else:
            try:
                invitelink = await client.export_chat_invite_link(message.chat.id)
            except ChatAdminRequired:
                return await msg.edit_text(
                    f"**لا توجد صلاحية (رابط الدعوة) لإضافة المساعد {userbot.mention} هنا.. 🥀**"
                )
            except InviteRequestSent:
                try:
                    await app.approve_chat_join_request(message.chat.id, userbot.id)
                except Exception as e:
                    return await msg.edit(
                        f"**فشلت محاولة دعوة المساعد {userbot.mention} للمجموعة.. 🥀**\n\n**السبب :** `{e}`"
                    )
            except Exception as ex:
                if "channels.JoinChannel" in str(ex) or "Username not found" in str(ex):
                    return await msg.edit_text(
                        f"**لا توجد صلاحيات كافية لدعوة المساعد {userbot.mention} للمجموعة.. 🥀**"
                    )
                else:
                    return await msg.edit_text(
                        f"**فشلت دعوة المساعد {userbot.mention} للمجموعة.. 🥀**\n\n**السبب :** `{ex}`"
                    )
        if invitelink.startswith("https://t.me/+"):
            invitelink = invitelink.replace("https://t.me/+", "https://t.me/joinchat/")
        await msg.edit_text(
            f"**يرجى الانتظار.. جاري إضافة المساعد {userbot.mention} لتشغيل الراديو.. ⚡**"
        )
        try:
            await userbot.join_chat(invitelink)
            await asyncio.sleep(2)
            await msg.edit_text(
                f"**تم انضمام المساعد {userbot.mention} بنجاح، جاري بدء البث.. ✨📻**"
            )
        except UserAlreadyParticipant:
            pass
        except InviteRequestSent:
            await app.approve_chat_join_request(message.chat.id, userbot.id)
        except Exception as ex:
            return await msg.edit_text(
                f"**حدث خطأ أثناء دعوة المساعد {userbot.mention} للمجموعة.. 🥀**\n\n**السبب :** `{ex}`"
            )

    await msg.delete()
    station_name = " ".join(message.command[1:])
    RADIO_URL = RADIO_STATION.get(station_name)

    if RADIO_URL:
        language = await get_lang(message.chat.id)
        _ = get_string(language)

        mystic = await message.reply_text(_["play_1"])
        await stream(
            _,
            mystic,
            message.from_user.id,
            RADIO_URL,
            message.chat.id,
            message.from_user.mention,
            message.chat.id,
            video=None,
            streamtype="index",
        )
        return await play_logs(message, streamtype="M3u8 or Index Link")
    else:
        await message.reply(
            f"**يرجى كتابة اسم المحطة بعد الأمر.. 💝**\n\n**المحطات المتاحة هي:**\n{valid_stations}"
        )


__MODULE__ = "Rᴀᴅɪᴏ"
__HELP__ = f"\n/radio [اسم المحطة] - **لتشغيل الراديو في الدردشة الصوتية**\n\n**قائمة المحطات المتاحة:**\n{valid_stations}"

➻ sᴏᴜʀᴄᴇ : بُودَا | ʙᴏᴅᴀ
