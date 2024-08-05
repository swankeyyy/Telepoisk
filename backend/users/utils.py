from .models import User

def _get_or_create_user_from_tg(request):
    """takes data from request from TG bot when user clicked start button
    and create new user if he is not exists"""
    telegram_id = request.POST.get('telegram_id')
    username = request.POST.get('username')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    if not username:
        username = first_name + last_name
    User.objects.get_or_create(telegram_id=telegram_id,
                               username=username, first_name=first_name, last_name=last_name)



