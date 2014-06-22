import Db
from User import *
from django.shortcuts import render
from django.shortcuts import redirect

def users(request):
  if ('connected' in request.session):
    return render(request, "users.html", {'datas': request.session['trombi'], 'sess': request.session})
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
        if (data['location'] != 'Hors-Ligne'):
          Db.update(uid=user, fields = {'latest_location': data['location'],
                                        'latest_activity': 1})
        latest = Db.get(uid=user, fields = ('latest_activity',))
        if ('latest_activity' in latest) and (latest['latest_activity']):
          data['latest'] = '%s @ (%s)' % (latest['latest_activity'], data['location']) 
    return render(request, "profile.html", {'data': data, 'sess' : request.session})
  else:
    return redirect('/login')
