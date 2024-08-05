import telebot
from telebot import types
import requests

from telegram.utils import _get_user_data, _get_header_from_response, _get_photo_from_response

# token and backend_url settings
token = '7442563954:AAHhLc8rh1R07rw3dIoHPF9uNfVRVREarQU'
bot = telebot.TeleBot(token)
backend_url = 'http://127.0.0.1:8000/api/'
media_backend_url = 'http://127.0.0.1:8000/'
# buttons for start page
movie_offer = types.InlineKeyboardMarkup()
btn = types.InlineKeyboardButton(text='Подобрать случайный фильм', callback_data='get_movie')
movie_offer.add(btn)


# kb = types.InlineKeyboardMarkup(row_width=2)
# btn1 = types.InlineKeyboardButton(text='next', callback_data='next')
# btn2 = types.InlineKeyboardButton(text='reg', callback_data='reg')

# kb.add(btn1, btn2)


@bot.callback_query_handler(func=lambda call: call.data == 'get_movie')
def get_movie(call):
    """get random movie from backend"""
    user_id = call.from_user.id
    data = {
        'telegram_id': user_id,
    }
    response = requests.get(backend_url + 'random_movie/', data)
    header = _get_header_from_response(response)
    bot.send_message(call.message.chat.id, header, parse_mode='HTML')
    photo = _get_photo_from_response(response)
    bot.send_photo(call.message.chat.id, photo, parse_mode='HTML')
    description = response.json()['description']
    bot.send_message(call.message.chat.id, description)




@bot.message_handler(commands=['start'])
def start(message):
    """by /start send request to backend and check current user in database
    if user is not exists, send data for create new instance
    """
    data = _get_user_data(message)
    try:
        response = requests.post(backend_url + 'register/', data=data)
        if response.status_code == 200:
            bot.send_message(message.chat.id,
                             'Добро пожаловать в TelePoisk! Если нет идей что посмотреть вечером, попробуй нашу подборку! Если есть что предложить, предлагай!',
                             reply_markup=movie_offer)

    except Exception as e:
        print(e)
        bot.send_message(message.chat.id, 'Что-то пошло не так( попробуйте позже!')


bot.polling(none_stop=True)
