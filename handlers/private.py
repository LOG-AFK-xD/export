from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    
    await message.reply_text(
        f"""<b>Hi {message.from_user.mention} ðï¸!</b>

I'á´ TÊá´ KÉªá´Êá´ RoÊá´á´! A Pá´á´¡á´ÊÒá´Ê Bá´á´ á´á´ PÊá´Ê Má´sÉªá´ ÉªÉ´ Yá´á´Ê GÊá´á´á´ Vá´Éªá´á´ CÊá´á´ ð! 

AÊsá´ I Êá´á´ á´ á´á´Êá´ Òá´á´á´á´Êá´s! PÊá´á´sá´ ÊÉªá´ á´É´  á´á´ sá´á´ á´Êá´á´ ð!...

Dá´á´ á´Êá´á´á´Ê BÊ : [ððð ððð](https://t.me/Log_out_xd)ð[ðððð ððð](https://t.me/Evil_boy_xd)**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "â¨Aá´á´ Má´ Tá´ Yá´á´Ê GÊá´á´á´â¨", url="https://t.me/Kiara_ro_bot?startgroup=true")
                  ],[
                    InlineKeyboardButton(
                        "ð·Sá´á´á´á´Êá´ GÊá´á´á´ð¥", url="https://t.me/The_SECRET_worlds"
                    ),
                    InlineKeyboardButton(
                        "Sá´á´á´á´Êá´ CÊá´É´É´á´Ê", url="https://t.me/The_Blaze_Network"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "Há´Êá´ & Cá´á´á´á´É´á´s", url="https://telegra.ph/BLAZE-MUSIC-BOT-12-09"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("hexor") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**ðð¼ð ð¢ð»ð¹ð¶ð»ð²..ð**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ð¦ðð½ð½ð¼ð¿ð", url="https://t.me/kiara_support")
                ]
            ]
        )
   )
