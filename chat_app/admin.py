from django.contrib import admin
from chat_app.models import Chat, Message

# Register your models here.
admin.site.register(Chat)
admin.site.register(Message)