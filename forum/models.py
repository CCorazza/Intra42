from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)
    parent_category = models.ForeignKey('Category', blank=True, null=True)

    def __str__(self):
        return self.name

class Thread(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey('Category')
    author = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title

class Message(models.Model):
    thread = models.ForeignKey('Thread')
    author = models.CharField(max_length=200)
    content = models.CharField(max_length=10000)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.content[:50]

class Comment(models.Model):
    message = models.ForeignKey('Message')
    author = models.CharField(max_length=200)
    content = models.CharField(max_length=10000)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.content[:50]
