from aiogram import types
from aiogram.types import InputFile
from loader import dp, base, bot
from keyboards.inline.inline_buttons import share_buttons



# Echo bot
@dp.message_handler(text='Offer Works')
async def bot_help(message: types.Message):
    offer_works = base.select_offer_works()
    for offer_work in offer_works:
        photo_file = InputFile(path_or_bytesio=f"media/{offer_work[7]}")
        
        caption = f"""<b>🖇Nomi: {offer_work[1]}</b> \n📍Manzili: {offer_work[2]} \n🗝Eski narxi: {offer_work[3]} \n🔑Yangi narxi: {offer_work[4]} \n📋Umumiy maydon: {offer_work[9]}"""
        url = f"https://uptownbackend.pythonanywhere.com/properties/{offer_work[0]}/"
        caption += "\n\n☎️Aloqa: @Asadbek_Muxtorov"

        await message.reply_photo(
            photo_file, caption=caption,
            reply_markup=share_buttons(url)
        )
                        
    await message.answer(text='Raxmat')

@dp.message_handler(text='Happy Clients')
async def bot_help(message: types.Message):
    happy_clients = base.select_happy_clients()
    for happy_client in happy_clients:
        print(happy_client)
        photo_file = InputFile(path_or_bytesio=f"media/{happy_client[3]}")
        caption = f"""Ismi: <b>{happy_client[1]}</b> \nLavozimi: <b>{happy_client[2]}</b> \nFikri: <b>{happy_client[4]}</b>"""
        caption += "\n\n☎️Aloqa: @Asadbek_Muxtorov"
        await message.reply_photo(
            photo_file,
            caption=caption,
        )

    await message.answer(text='Raxmat')


@dp.message_handler(text='Agents')
async def bot_help(message: types.Message):
    agents = base.select_agents()
    for agent in agents:
        print('#'*10 + 'agents' + '#' *10)
        photo_file = InputFile(path_or_bytesio=f"media/{agent[2]}")
        caption = f"Ismi: <b>{agent[1]}</b>"
        caption += "\n\n☎️Aloqa: @Asadbek_Muxtorov"
        await message.reply_photo(
            photo_file,
            caption=caption
        )
        print(agent)
        

    await message.answer(text='Raxmat')

def return_username(author_id: int) -> str:
    auth_users = base.select_auth_users()
    for auth_user in auth_users:
        if auth_user[0] == author_id:
            return auth_user[4]


@dp.message_handler(text='Resent Blog')
async def bot_help(message: types.Message):
    blogs = base.select_resent_blogs()
    users = base.select_auth_users()
    print(users)
    for blog in blogs:
        photo_file = InputFile(path_or_bytesio=f"media/{blog[4]}")
        caption = f"Sarlavha: <b>{blog[1]}</b> \nMuallif: <b>{return_username(blog[5])}</b> \nTo'liq: <b>{blog[3]}</b>"
        caption += "\n\n☎️Aloqa: @Asadbek_Muxtorov"
        await message.reply_photo(
            photo_file,
            caption = caption 
        )
        

    await message.answer(text='Raxmat')