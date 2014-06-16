from django.db import models
from django.contrib.auth.models import User

class Ticket(models.Model):
    title = models.CharField(max_length=200)
    closed = models.BooleanField(default=False)
    admin = models.ForeignKey(User, related_name='ticket_admin')
    author = models.ForeignKey(User, related_name='ticket_user')
    pub_date = models.DateTimeField('date published')
    mod_date = models.DateTimeField('date last modified')

    def __str__(self):
        return self.title

class Message(models.Model):
    ticket = models.ForeignKey(Ticket)
    author = models.ForeignKey(User)
    content = models.CharField(max_length=10000)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.content[:50]
