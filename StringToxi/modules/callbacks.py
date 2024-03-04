from pyrogram import filters
from pyrogram.types import CallbackQuery

from pyrogram import filters
from pyrogram.types import Message

from StringToxi import Anony
from StringToxi.utils import gen_key
from StringToxi.modules.gen import gen_session

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ReplyKeyboardMarkup

from StringToxi import Anony
from StringToxi.utils import add_served_user, keyboard



@Anony.on_callback_query(
    filters.regex(pattern=r"^(gensession|pyrogram|pyrogram1|telethon)$")
)
async def cb_choose(_, cq: CallbackQuery):
    await cq.answer()
    query = cq.matches[0].group(1)
    if query == "gensession":
        return await cq.message.reply_text(
            text="⭓ 𝑺𝑶𝑼𝑹𝑪𝑬 𝑻𝑶𝑿𝑰𝑪\n╮⦿ هييه ياروع اختار ما تشاء\n╯⦿ من جلسات متطوره",
            reply_markup=gen_key,
        )
    elif query.startswith("pyrogram") or query.startswith("telethon"):
        try:
            if query == "pyrogram":
                await gen_session(cq.message, cq.from_user.id)
            elif query == "pyrogram1":
                await gen_session(cq.message, cq.from_user.id, old_pyro=True)
            elif query == "telethon":
                await gen_session(cq.message, cq.from_user.id, telethon=True)
        except Exception as e:
            await cq.edit_message_text(e, disable_web_page_preview=True)




@Anony.on_callback_query(
    filters.regex(pattern=r"^gahhsk$")
)
async def f_staryyyit(_, cq: CallbackQuery):
    await cq.message.reply_text(
            text=f"""⭓ 𝑺𝑶𝑼𝑹𝑪𝑬 𝑻𝑶𝑿𝑰𝑪\n╮⦿ مرحباً بك عزيزي\n╯⦿ اتبع التعليمات لستخراج الصحيح\n╮⦿ اولا قم بضغط علي : sᴇssɪᴏɴ\n╯⦿ ثانياً: اختار اصدار الذي تريده\n╮⦿ ثالثاً قم بارسال: ᴀᴘɪ ɪᴅ\n╯⦿ رابعاً  قم بارسال: ᴀᴘɪ ʜᴀsʜ\n╮⦿ خامساً قم بارسال رقم الهاتف\n╯⦿ ثم ارسال كود التحقق هكذا 1 2 3 4\n╯⦿ ثم ارسل كلمه المرور\n╮⦿ ثم اذهب للرسال المحفوظه\n╯⦿ وتفقد الجلسه تم استخرجها""",
        reply_markup=keyboard,
    )
    await cq.edit_message_text(e, disable_web_page_preview=True)