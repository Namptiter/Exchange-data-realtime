from django.contrib import admin

# Register your models here.
from .models import Message

class MessageAdmin(admin.ModelAdmin):
	list_display = ('user_name','message')
admin.site.register(Message, MessageAdmin)