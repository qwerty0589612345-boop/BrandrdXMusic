from BrandrdXMusic import app 
import asyncio
import random
from pyrogram import Client, filters
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.errors import UserNotParticipant
from pyrogram.types import ChatPermissions

spam_chats = []

EMOJI = [ "🦋🦋🦋🦋🦋",
          "🧚🌸🧋🍬🫖",
          "🥀🌷🌹🌺💐",
          "🌸🌿💮🌱🌵",
          "❤️💚💙💜🖤",
          "💓💕💞💗💖",
          "🌸💐🌺🌹🦋",
          "🍔🦪🍛🍲🥗",
          "🍎🍓🍒🍑🌶️",
          "🧋🥤🧋🥛🍷",
          "🍬🍭🧁🎂🍡",
          "🍨🧉🍺☕🍻",
          "🥪🥧🍦🍥🍚",
          "🫖☕🍹🍷🥛",
          "☕🧃🍩🍦🍙",
          "🍁🌾💮🍂🌿",
          "🌨️🌥️⛈️🌩️🌧️",
          "🌷🏵️🌸🌺💐",
          "💮🌼🌻🍀🍁",
          "🧟🦸🦹🧙👸",
          "🧅🍠🥕🌽🥦",
          "🐷🐹🐭🐨🐻‍❄️",
          "🦋🐇🐀🐈🐈‍⬛",
          "🌼🌳🌲🌴🌵",
          "🥩🍋🍐🍈🍇",
          "🍴🍽️🔪🍶🥃",
          "🕌🏰🏩⛩️🏩",
          "🎉🎊🎈🎂🎀",
          "🪴🌵🌴🌳🌲",
          "🎄🎋🎍🎑🎎",
          "🦅🦜🕊️🦤🦢",
          "🦤🦩🦚🦃🦆",
          "🐬🦭🦈🐋🐳",
          "🐔🐟🐠🐡🦐",
          "🦩🦀🦑🐙🦪",
          "🐦🦂🕷️🕸️🐚",
          "🥪🍰🥧🍨🍨",
          " 🥬🍉🧁🧇",
        ]

SHAYRI = [ 
    " 🌺**الكلمة الحلوة بتفتح أبواب مقفولة، خليك دايما صاحب كلمة طيبة.**🌺 ",
    " 🌺**الأصول مش مجرد كلام، الأصول أفعال وإنت سيد من يعملها.**🌺 ",
    " 🌺**يا رب أيامك كلها تكون مبهجة وزي الفل يا غالي.**🌺 ",
    " 🌺**الصحاب في الشدة بيبانوا، وإنت دايما واقف وقفة رجالة.**🌺 ",
    " 🌺**الضحكة الصافية طالعة من قلب أبيض، وقلبك مفيش أنظف منه.**🌺 ",
    " 🌺**خليك واثق إن اللي جاي أحسن، وربنا شايلك كل خير.**🌺 ",
    " 🌺**من لزم الاستغفار جعل الله له من كل هم فرجاً، اذكر الله.**🌺 ",
    " 🌺**الرزق يحب السعي، وإنت دايما مجتهد وتستاهل كل خير.**🌺 ",
    " 🌺**يا بخت الجروب ده بوجود شخص محترم وزي العسل زيك.**🌺 ",
    " 🌺**ساعات الهدوء بيكون أجمل بكتير من دوشة الكلام الكتير.**🌺 ",
    " 🌺**منور الدنيا بضحكتك، ربنا يديمها عليك نعمة.**🌺 ",
    " 🌺**الجدعنة مدرسة وإنت المدير بتاعها يا وحش.**🌺 ",
    " 🌺**يا رب يرزقك سعادة لا تنتهي وراحة بال ملوش حدود.**🌺 ",
    " 🌺**خليك دايما منبع أمل لكل اللي حواليك.**🌺 ",
    " 🌺**سهرة سعيدة مع أحلى وأغلى ناس في الدنيا.**🌺 ",
    " 🌺**الاحترام هو اللي بيبني العلاقات، وإنت محترم لابعد حد.**🌺 ",
    " 🌺**يا رب يحفظك لأهلك ولصحابك ويبعد عنك أي شر.**🌺 ",
    " 🌺**الجمال الحقيقي هو جمال الروح اللي بتبان في تعاملك.**🌺 ",
    " 🌺**الدنيا لسة بخير طول ما فيها ناس بقلوب طيبة زيك.**🌺 ",
    " 🌺**كل حاجة بتعدي، المهم إننا نفضل دايما سند لبعض.**🌺 "
]

@app.on_message(filters.command(["shayari", "شعر"], prefixes=["/", "@", "#"]))
async def mentionall(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("الأمر ده للمجموعات بس يا نجم.")

    is_admin = False
    try:
        participant = await client.get_chat_member(chat_id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
            
    if not is_admin:
        return await message.reply("يا بيبي إنت مش أدمن، المنشن للمشرفين بس.")

    if message.reply_to_message and message.text:
        return await message.reply("استخدم /shayari أو رد على رسالة عشان أبدأ.")
    elif message.text:
        mode = "text_on_cmd"
        msg = message.text
    elif message.reply_to_message:
        mode = "text_on_reply"
        msg = message.reply_to_message
        if not msg:
            return await message.reply("رد على رسالة عشان أعملك منشن رايق...")
    else:
        return await message.reply("استخدم الأمر صح عشان أهبدلك الشعر.")

    if chat_id in spam_chats:
        return await message.reply("فيه عملية شغالة دلوقتي، وقفها الأول.")
        
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += "<a href='tg://user?id={}'>{}</a>".format(usr.user.id, usr.user.first_name)

        if usrnum == 1:
            if mode == "text_on_cmd":
                txt = f"{usrtxt} {random.choice(SHAYRI)}\n\nBY: **Source Boda** 👣"
                await client.send_message(chat_id, txt)
            elif mode == "text_on_reply":
                await msg.reply(f"[{random.choice(EMOJI)}](tg://user?id={usr.user.id})")
            await asyncio.sleep(4)
            usrnum = 0
            usrtxt = ""
            
    try:
        spam_chats.remove(chat_id)
    except:
        pass

@app.on_message(filters.command(["cancelshayari", "shayarioff", "وقف_الشعر"]))
async def cancel_spam(client, message):
    if not message.chat.id in spam_chats:
        return await message.reply("مفيش حاجة شغالة حالياً يا وحش.")
        
    is_admin = False
    try:
        participant = await client.get_chat_member(message.chat.id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
            
    if not is_admin:
        return await message.reply("الأمر للأدمن بس، متدخلش في اللي مالكش فيه.")
    else:
        try:
            spam_chats.remove(message.chat.id)
        except:
            pass
        return await message.reply("✅ تم إيقاف عملية المنشن بنجاح.\n\n👣 **Source Boda** 💗")
