import telebot
import os
from telebot import types
import requests
from utils import _get_user_data, _get_header_from_response, _get_photo_from_response, _get_id_for_bookmarks

# token and backend_url settings
token = os.environ.get('TOKEN')
bot = telebot.TeleBot(token)

#url settings
backend_url = os.environ.get('URL')
media_backend_url = os.environ.get('MEDIA_URL')

# buttons for start page
movie_offer = types.InlineKeyboardMarkup()
btn = types.InlineKeyboardButton(text='Подобрать случайный фильм', callback_data='get_movie')
movie_offer.add(btn)

# buttons for favorites and aborted list
user_movie_list = types.InlineKeyboardMarkup(row_width=2)
btn2 = types.InlineKeyboardButton(text='Добавить в закладки', callback_data='add_to_favorite')
btn3 = types.InlineKeyboardButton(text='Неинтересно', callback_data='add_to_aborted')
btn4 = types.InlineKeyboardButton(text='Закладки', callback_data='get_favorites')
user_movie_list.add(btn2, btn3, btn4)

#button for users favorite
favorite_list = types.InlineKeyboardMarkup()
btn4 = types.InlineKeyboardButton(text='Посмотреть свои закладки', callback_data='get_favorites')
favorite_list.add(btn4)

#temporary data for user
d = {}

@bot.callback_query_handler(func=lambda call: call.data == 'get_movie')
def get_movie(call):
    """get random movie from backend"""
    user_id = call.from_user.id
    data = {
        'telegram_id': user_id,
    }
    response = requests.get(backend_url + 'random_movie/', data)

    movie_id = response.json().get('id', None)
    if movie_id:
        #set a temp info about user id and movie id for favorite and ignor
        d[user_id] = movie_id

        header = _get_header_from_response(response)
        bot.send_message(call.message.chat.id, header, parse_mode='HTML')
        photo = _get_photo_from_response(response)
        if photo:
            bot.send_photo(call.message.chat.id, photo, parse_mode='HTML')

        description = response.json()['description']
        bot.send_message(call.message.chat.id, description, reply_markup=movie_offer)
        bot.send_message(call.message.chat.id, '<i>Выберите действие</i>\n',
                         reply_markup=user_movie_list, parse_mode='HTML')

    else:
        bot.send_message(call.message.chat.id, 'Пока нет новых поступлений(', reply_markup=favorite_list)


@bot.callback_query_handler(func=lambda call: call.data == 'add_to_favorite')
def add_to_favorite(call):
    """get user_id and movie_id from dict 'd' and send to backend"""
    try:
        data = _get_id_for_bookmarks(call, d, 'favorites')

        response = requests.post(backend_url + 'add_to_list/', data)
        if response.status_code == 200:
            bot.send_message(call.message.chat.id, 'Добавлено в избранное', reply_markup=movie_offer)
    except Exception as e:
        print(e)
        bot.send_message(call.message.chat.id, 'Что-то пошло не так(')



@bot.callback_query_handler(func=lambda call: call.data == 'add_to_aborted')
def add_to_aborted(call):
    """get user_id and movie_id from dict 'd' and send to backend"""
    try:
        data = _get_id_for_bookmarks(call, d, 'aborted')

        response = requests.post(backend_url + 'add_to_list/', data)
        if response.status_code == 200:
            bot.send_message(call.message.chat.id, 'Понятно, больше не попадется', reply_markup=movie_offer)
    except Exception as e:
        print(e)
        bot.send_message(call.message.chat.id, 'Что-то пошло не так(', reply_markup=movie_offer)


@bot.callback_query_handler(func=lambda call: call.data == 'get_favorites')
def get_favorites(call):
    data = {
        'telegram_id': call.from_user.id,
    }
    response = requests.get(backend_url + 'get_favorites/', data)
    mes = 'Список закладок пока пуст'
    if response.status_code == 200:
        mes = ''
        for item in response.json():
            mes += f"-----{item['name']}  - {item['year']}\n"

    bot.send_message(call.message.chat.id, mes, reply_markup=movie_offer)





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
        bot.send_message(message.chat.id, 'Что-то пошло не так( попробуйте позже!', reply_markup=movie_offer)


bot.infinity_polling()
