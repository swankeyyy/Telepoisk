import telebot
from telebot import types
import requests
token = '7442563954:AAHhLc8rh1R07rw3dIoHPF9uNfVRVREarQU'
bot = telebot.TeleBot(token)



kb = types.InlineKeyboardMarkup(row_width=2)
btn1 = types.InlineKeyboardButton(text='next', callback_data='next')
btn2 = types.InlineKeyboardButton(text='reg', callback_data='reg')

kb.add(btn1, btn2)


@bot.callback_query_handler(func=lambda call: call.data == 'reg')
def callback_handler(call):
    user_id = call.from_user.id
    first_name = call.from_user.first_name
    username = call.from_user.username if call.from_user.username else ''
    last_name = call.from_user.last_name
    data = {
        'telegram_id': user_id,
        'first_name': first_name,
        'username': username,
        'last_name': last_name,
    }

    response = requests.post('http://127.0.0.1:8000/api/register/', data=data)
    print(response.status_code)

    bot.send_message(call.message.chat.id, 'hello kitty')



@bot.message_handler(commands=['start'])
def start(message):
    print(message.from_user.id)
    bot.send_message(message.chat.id, message, reply_markup=kb)

bot.polling()





