import telebot
from telebot import types
import requests

# token and backend_url settings
token = '7442563954:AAHhLc8rh1R07rw3dIoHPF9uNfVRVREarQU'
bot = telebot.TeleBot(token)
backend_url = 'http://127.0.0.1:8000/api/'

# buttons for start page
movie_offer = types.InlineKeyboardMarkup()
btn = types.InlineKeyboardButton(text='Подобрать фильм', callback_data='get_movie')
movie_offer.add(btn)


# kb = types.InlineKeyboardMarkup(row_width=2)
# btn1 = types.InlineKeyboardButton(text='next', callback_data='next')
# btn2 = types.InlineKeyboardButton(text='reg', callback_data='reg')

# kb.add(btn1, btn2)


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

    response = requests.post(backend_url + 'register/', data=data)
    print(response.status_code)

    bot.send_message(call.message.chat.id, 'Добро пожаловать в TelePoisk, если тебе скучно и нет идей!')


@bot.message_handler(commands=['start'])
def start(message):
    """by /start send request to backend and check current user in database
    if user is not exists, send data for create new instance
    """
    user_id = message.from_user.id
    first_name = message.from_user.first_name if message.from_user.first_name else ''
    username = message.from_user.username if message.from_user.username else ''
    last_name = message.from_user.last_name if message.from_user.last_name else ''
    data = {
        'telegram_id': user_id,
        'first_name': first_name,
        'username': username,
        'last_name': last_name,
    }

    try:
        response = requests.post('http://127.0.0.1:8000/api/register/', data=data)
        if response.status_code == 200:
            bot.send_message(message.chat.id,
                             'Добро пожаловать в TelePoisk! Если нет идей что посмотреть вечером, попробуй нашу подборку! Если есть что предложить, предлагай!',
                             reply_markup=movie_offer)

    except Exception as e:
        print(e)
        bot.send_message(message.chat.id, 'Что-то пошло не так( попробуйте позже!')


bot.polling(none_stop=True)
