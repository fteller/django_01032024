from django.contrib import admin
from contact.models import Message


# Register your models here.
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'subject', 'email', 'message', 'created_date', 'updated_date']
    search_fields = ['name', 'subject', 'email', 'message']

    class Meta:
        model = Message
