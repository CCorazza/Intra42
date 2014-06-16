from django.db import models
from django.contrib import admin

class Student(models.Model):
  uid = models.CharField(max_length=255, unique=True)
  latest_activity = models.CharField(max_length=512)
  latest_location = models.CharField(max_length=512)
  email_perso = models.CharField(max_length=512)
  privilege = models.CharField(max_length=512)
  facebook = models.CharField(max_length=512)
  twitter = models.CharField(max_length=512)
  website = models.CharField(max_length=512)
  google = models.CharField(max_length=512)

  def __unicode__(self):
    return u"%s" % self.uid

admin.site.register(Student)
