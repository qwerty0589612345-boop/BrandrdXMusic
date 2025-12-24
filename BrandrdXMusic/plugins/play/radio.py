import logging
import asyncio
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

# قنوات الراديو المتاحة
RADIO_STATION = {
    "قرآن كريم": "https://stream.radiojar.com/8s5u5tpdtwzuv",
    "نجوم إف إم": "https://shoutcast.nrp.io/nogoum/stream",
    "Air Bilaspur": "http://air.pc.cdn.bitgravity.com/air/live/pbaudio110/playlist.m3u8",
    "Air Raipur": "http://air.pc.cdn.bitgravity.com/air/live/pbaudio118/playlist.m3u8",
    "Capital FM": "http://media-ice.musicradio.com/CapitalMP3?.mp3&listening-from-radio-garden=1616312105154",
    "English": "https://hls-01-regions.emgsound.ru/11_msk/playlist.m3u8",
    "Mirchi": "http://peridot.streamguys.com:7150/Mirchi",
    "Radio Today": "http://stream.zenolive.com/8wv4d8g4344tv",
    "YouTube": "https://www.youtube.com/live/eu191hR_LEc",
    "Zee News": "https://www.youtube.com/live/TPcmrPrygDc",
    "Aaj Tak": "https://www.youtube.com/live/Nq2wYlWFucg",
}

valid_stations = "\n".join([f"• `{name}`" for name in sorted(RADIO_STATION.keys())])

@app.on_message(
    filters.command(["radioplayforce", "radio", "cradio"])
    & filters.group
    & ~BANNED_USERS
)
async def radio(client, message: Message):
    msg = await message.reply_text("**ثواني يا حُب.. جاري التحضير ✨**")
    try:
        try:
            userbot = await get_assistant(message.chat.id)
            get = await app.get_chat_member(message.chat.id, userbot.id)
        except ChatAdminRequired:
            return await msg.edit_text(
                f"**معنديش صلاحية أضيف المساعد {userbot.mention} للجروب هنا، ارفعني أدمن يا غالي.**"
            )
        if get.status == ChatMemberStatus.BANNED:
            return await msg.edit_text(
                text=f"**المساعد {userbot.mention} مطرود من الجروب هنا 📛**\n\n🆔 الأيدي: `{userbot.id}`\n👤 الاسم: {userbot.mention}\n\n**فكه من البلوك وجرب تاني يا حُب.**",
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
                    f"**معنديش صلاحية أضيف المساعد {userbot.mention} للجروب هنا، ارفعني أدمن يا غالي.**"
                )
            except InviteRequestSent:
                try:
                    await app.approve_chat_join_request(message.chat.id, userbot.id)
                except Exception as e:
                    return await msg.edit(
                        f"**مش عارف أضيف المساعد {userbot.mention} للجروب.**\n\n**السبب :** `{e}`"
                    )
            except Exception as ex:
                return await msg.edit_text(
                    f"**مش عارف أضيف المساعد {userbot.mention} للجروب.**\n\n**السبب :** `{ex}`"
                )
        
        if invitelink.startswith("https://t.me/+"):
            invitelink = invitelink.replace("https://t.me/+", "https://t.me/joinchat/")
        
        await msg.edit_text(f"**ثواني بدخل المساعد {userbot.mention} للجروب.. ⚡**")
        try:
            await userbot.join_chat(invitelink)
            await asyncio.sleep(2)
            await msg.edit_text(f"**المساعد دخل بنجاح، جاري تشغيل الراديو... ✨**")
        except UserAlreadyParticipant:
            pass
        except Exception as ex:
            return await msg.edit_text(f"**فشل انضمام المساعد.**\n\n**السبب:** `{ex}`")

    await msg.delete()
    station_name = " ".join(message.command[1:])
    RADIO_URL = RADIO_STATION.get(station_name)
    
    if RADIO_URL:
        language = await get_lang(message.chat.id)
        _ = get_string(language)
        playty = await get_playtype(message.chat.id)
        
        if playty != "Everyone":
            if message.from_user.id not in SUDOERS:
                admins = adminlist.get(message.chat.id)
                if not admins or message.from_user.id not in admins:
                    return await message.reply_text("**الأمر ده للأدمن بس يا حُب 💖**")

        if message.command[0][0] == "c":
            chat_id = await get_cmode(message.chat.id)
            if chat_id is None:
                return await message.reply_text("**لازم تربط القناة الأول يا غالي.**")
            try:
                chat = await app.get_chat(chat_id)
                channel = chat.title
            except:
                return await message.reply_text("**مش لاقي القناة المربوطة.**")
        else:
            chat_id = message.chat.id
            channel = None

        mystic = await message.reply_text("**جاري تشغيل الراديو.. استمتع ✨**")
        try:
            await stream(
                _,
                mystic,
                message.from_user.id,
                RADIO_URL,
                chat_id,
                message.from_user.mention,
                message.chat.id,
                video=None,
                streamtype="index",
            )
        except Exception as e:
            return await mystic.edit_text(f"**حدث خطأ:** `{e}`")
        
        return await play_logs(message, streamtype="راديو مباشر")
    else:
        await message.reply(
            f"**اكتب اسم محطة الراديو يا غالي بعد الأمر، زي كدة:**\n`/radio قرآن كريم`\n\n**المحطات المتاحة حالياً:**\n{valid_stations}\n\n➻ sᴏᴜʀᴄᴇ : بُودَا | ʙᴏᴅᴀ"
        )

__MODULE__ = "الراديو"
__HELP__ = f"\n**/radio [اسم المحطة]** - لتشغيل الراديو في المكالمة\n\n**المحطات المتاحة:**\n{valid_stations}\n\n➻ sᴏᴜʀᴄᴇ : بُودَا | ʙᴏᴅᴀ"

# ➻ sᴏᴜʀᴄᴇ : بُودَا | ʙᴏᴅᴀ
