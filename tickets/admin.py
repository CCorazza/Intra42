from django.contrib import admin

from tickets.models import Ticket, Message

admin.site.register(Ticket)
admin.site.register(Message)
