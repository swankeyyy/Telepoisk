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
        f"<b>{content['genre'][0]}</b>")
    return header


def _get_photo_from_response(response):
    """get url photo, save photo and send it for user"""
    photo = media_backend_url + response.json()['poster'][1:]
    img = requests.get(photo)
    photo_name = response.json()['name']
    img_file = open(f'images/{photo_name}', 'wb')
    img_file.write(img.content)
    img_file.close()
    p = open(f'images/{photo_name}', 'rb')
    return p
