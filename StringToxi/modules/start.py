from pyrogram import filters
from pyrogram.types import Message

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ReplyKeyboardMarkup

from StringToxi import Anony
from StringToxi.utils import add_served_user, keyboard


@Anony.on_message(filters.command("start") & filters.private & filters.incoming)
async def f_start(_, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/51e0f2e3033081588359a.jpg",
        caption=f"""⭓ 𝑺𝑶𝑼𝑹𝑪𝑬 𝑻𝑶𝑿𝑰𝑪\n╮⦿ مرحباً بك عزيزي : {message.from_user.first_name},\n╯⦿  اسمي : {Anony.mention},\n╮⦿ تم صنعي من قبل فيجا\n╯⦿ اعمل علي استخراج جلسات""",
        reply_markup=keyboard,
    )
    await add_served_user(message.from_user.id)



