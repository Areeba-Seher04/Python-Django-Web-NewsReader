from django.contrib import admin
from .models import Channel,FChannel
from django.contrib.auth.models import User

admin.site.register(Channel)

admin.site.register(FChannel)
