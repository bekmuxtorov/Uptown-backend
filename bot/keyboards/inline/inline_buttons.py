from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def share_buttons(url):
    share = InlineKeyboardMarkup(
        inline_keyboard= [
            [
                InlineKeyboardButton(
                    text = "Batafsil",
                    url = url
                )
            ]
        ]
    )

    return share