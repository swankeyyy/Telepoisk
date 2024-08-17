import requests

media_backend_url = 'http://127.0.0.1:8000/'


def _get_user_data(message):
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
    return data


def _get_header_from_response(response):
    content = response.json()

    header = (
        f"<i>Название:</i> <b>{content['name']}</b>\n<i>Год выпуска:</i> <b>{str(content['year'])}</b>\n<i>Жанр:</> "
        f"<b>{content['genre'][0]}</b>\n<i>Рейтинг Кинопоиска:</i> <b>{str(content['raiting'])}</b>")
    return header


def _get_photo_from_response(response):
    """get url photo, save photo and send it for user"""
    poster = response.json().get('poster', None)

    if poster:
        photo = media_backend_url + poster[1:]
        img = requests.get(photo)
        photo_name = response.json()['name']
        img_file = open(f'images/{photo_name}', 'wb')
        img_file.write(img.content)
        img_file.close()
        p = open(f'images/{photo_name}', 'rb')
        return p
    return False


def _get_id_for_bookmarks(call, d, type):
    user_id = call.from_user.id
    movie_id = d[user_id]
    data = {
        'telegram_id': user_id,
        'movie_id': movie_id,
        'list_type': type
    }
    return data
