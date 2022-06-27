from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from .info import get_movie

START_TEXT = """Merhaba {}
Sana istediğin Film ile ilgili Bilgi vereceğim"""

JOIN_BUTTONS = [
    InlineKeyboardButton(
        text='Blog Kanalıma katılın',
        url='https://telegram.me/mmagneto3'
    )
]

BUTTONS = InlineKeyboardMarkup(
    [JOIN_BUTTONS]
)

@Client.on_message(filters.private & filters.command(["start"]), group=-1)
async def start(bot, update):
    if update.text == "/start":
        await update.reply_text(
            text=START_TEXT.format(update.from_user.mention),
            reply_markup=BUTTONS,
            disable_web_page_preview=True,
            quote=True
        )
    else:
        movie = update.text.split(" ", 1)[1]
        await get_movie(bot, update, movie)
