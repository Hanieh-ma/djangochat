from django.contrib import admin
from chat.models import Conversations, Messages
# Register your models here.

admin.site.register(Conversations)
admin.site.register(Messages)