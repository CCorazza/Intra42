from django.contrib import admin
from forum.models import Category, Thread, Message, Comment

admin.site.register(Category)
admin.site.register(Thread)
admin.site.register(Message)
admin.site.register(Comment)
