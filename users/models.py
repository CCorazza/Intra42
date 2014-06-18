from django.db import models
from django.contrib import admin

class Student(models.Model):
  uid = models.CharField(max_length=255, unique=True)
  latest_activity = models.CharField(max_length=512, blank=True)
  latest_location = models.CharField(max_length=512, blank=True)
  email_perso = models.CharField(max_length=512, blank=True)
  privilege = models.CharField(max_length=512, blank=True)
  facebook = models.CharField(max_length=512, blank=True)
  twitter = models.CharField(max_length=512, blank=True)
  website = models.CharField(max_length=512, blank=True)
  google = models.CharField(max_length=512, blank=True)

  def __unicode__(self):
    return u"%s" % self.uid

admin.site.register(Student)
