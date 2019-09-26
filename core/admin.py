from django.contrib import admin

# Register your models here.
from .models import Message


class MessageAdmin(admin.ModelAdmin):
    list_display = ('client_id', 'topic', 'message',)


admin.site.register(Message, MessageAdmin)