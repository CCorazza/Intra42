from User import *
from django.shortcuts import render
from django.shortcuts import redirect

def users(request):
  u = User('jshkurti', '}jc?M72e')
  datas = []
  if (u.connected):
    datas = u.get_trombi()
  return render(request, "users.html", {'datas': datas})

def profile(request, user):
  u = User('jshkurti', '}jc?M72e')
  data = {}
  if (u.connected):
    data = u.get_info(user)
    if (data != {}):
      data['location'] = u.get_location(user)
  return render(request, "profile.html", {'data': data})
