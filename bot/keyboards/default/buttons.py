from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from loader import bot, base

start_buttons = ReplyKeyboardMarkup(
    keyboard= [
        [
            KeyboardButton(text='Offer Works'),
            KeyboardButton(text='Happy Clients')
        ],
        [
            KeyboardButton(text='Agents'),
            KeyboardButton(text='Resent Blog'),
        ]
    ],
    resize_keyboard=True
)

def baza_tugma(yozuvchilar: list[str]):
    index, i = 0, 0
    keys = []
    for yozuvchi in yozuvchilar:
        yozuvchi_nomi = yozuvchi[1]
        if i%2 == 0 and i != 0:
            index += 1

        if i % 2 == 0:
            keys.append([KeyboardButton(text=f'{yozuvchi_nomi}')])
        else:
            keys[index].append(KeyboardButton(text=f'{yozuvchi_nomi}'))
        i += 1
    
    keys.append([KeyboardButton(text='🔙Ortga')])
    return ReplyKeyboardMarkup(keyboard=keys, resize_keyboard=True)

# OFFER WORKS
offer_works = base.select_offer_works()
offer_works_buttons = baza_tugma(offer_works)