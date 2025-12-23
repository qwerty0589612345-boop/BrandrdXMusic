from pyrogram import Client, errors
from pyrogram.enums import ChatMemberStatus, ParseMode

import config

from ..logging import LOGGER


class Hotty(Client):
    def __init__(self):
        LOGGER(__name__).info(f"جاري تشغيل البوت...")
        super().__init__(
            name="BrandrdXMusic",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            in_memory=True,
            max_concurrent_transmissions=7,
        )

    async def start(self):
        await super().start()
        self.id = self.me.id
        self.name = self.me.first_name + " " + (self.me.last_name or "")
        self.username = self.me.username
        self.mention = self.me.mention

        try:
            await self.send_message(
                chat_id=config.LOGGER_ID,
                text=f"<u><b>» تم تشغيل البوت {self.mention} :</b><u>\n\nالأيدي : <code>{self.id}</code>\nالاسم : {self.name}\nاليوزر : @{self.username}",
            )
        except (errors.ChannelInvalid, errors.PeerIdInvalid):
            LOGGER(__name__).error(
                "البوت مش عارف يوصل لجروب السجل (Log). اتأكد إنك ضفت البوت في الجروب أو القناة الخاصة بالسجل."
            )

        except Exception as ex:
            LOGGER(__name__).error(
                f"حصلت مشكلة في الوصول لسجل البوت.\n السبب : {type(ex).__name__}."
            )

        a = await self.get_chat_member(config.LOGGER_ID, self.id)
        if a.status != ChatMemberStatus.ADMINISTRATOR:
            LOGGER(__name__).error(
                "يا ريت ترفع البوت مشرف (Admin) في جروب أو قناة السجل."
            )

        LOGGER(__name__).info(f"بوت الميوزك اشتغل باسم {self.name} ✨")

    async def stop(self):
        await super().stop()
