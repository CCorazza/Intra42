from django.db import models
from django.contrib import admin

class Module(models.Model):
  uid = models.CharField(max_length=255, unique=True)
  name = models.CharField(max_length=255, blank=True)
  description = models.CharField(max_length=20000, blank=True)
  semester = models.CharField(max_length=255, blank=True)
  credit = models.CharField(max_length=255, blank=True)
  begin = models.DateTimeField(blank=True)
  end = models.DateTimeField(blank=True)

  def __unicode__(self):
    return u"%s" % self.name

class Activity(models.Model):
  uid = models.CharField(max_length=255, unique=True)
  name = models.CharField(max_length=255, blank=True)
  description = models.CharField(max_length=20000, blank=True)
  belongs = models.CharField(max_length=255, blank=True)
  repo = models.CharField(max_length=512, blank=True)
  begin = models.DateTimeField(blank=True)
  end = models.DateTimeField(blank=True)

  def __unicode__(self):
    return u"%s" % self.name

class RegisteredModule(models.Model):
  username = models.CharField(max_length=255)
  module = models.CharField(max_length=255)

  def __unicode__(self):
    return u"%s" % self.username

class RegisteredActivity(models.Model):
  username = models.CharField(max_length=255)
  activity = models.CharField(max_length=255)

  def __unicode__(self):
    return u"%s" % self.username

admin.site.register(Module)
admin.site.register(Activity)
admin.site.register(RegisteredModule)
admin.site.register(RegisteredActivity)
