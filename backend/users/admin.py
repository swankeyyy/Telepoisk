from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from django.utils.safestring import mark_safe


class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'username', 'last_login', 'telegram_id')
    list_display_links = ('id', 'username', 'telegram_id')



admin.site.register(User, CustomUserAdmin)

admin.site.site_title = "TelePoisk"
admin.site.site_header = "lets see"