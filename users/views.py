from User import *
from django.shortcuts import render
from django.shortcuts import redirect

def users(request):
  if ('connected' in request.session):
    return render(request, "users.html", {'datas': request.session['trombi']})
  else:
    return redirect('/login')

def profile(request, user):
  if ('connected' in request.session):
    u = User(request.session['username'], request.session['password'])
    data = {}
    if (u.connected):
      data = u.get_info(user)
      if (data != {}):
        data['location'] = u.get_location(user)
    return render(request, "profile.html", {'data': data})
  else:
    return redirect('/login')
