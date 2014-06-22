from django import http
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from auth.forms import LoginForm#, RegisterForm
from users.User import User

#def login_user(request, username, password):
#    user = authenticate(username=username, password=password)
#    if user is not None:
#        login(request, user)
#        return True
#    return False

def login_user(request, username, password):
  user = authenticate(username=username, password=password)
  if user is not None:
    login(request, user)
    return True
  return False

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            u = User(username, password)
            if (u.connected):
                request.session['connected'] = True
                request.session['username'] = username
                request.session['password'] = password
                request.session['trombi'] = u.get_trombi()
                request.session['infos'] = u.infos
                login_user(request, username, password)
                return http.HttpResponseRedirect('/')
    else:
        form = LoginForm()
    return render(request, 'auth/login.html', {'form' : form})

def logout_view(request):
    if ('connected' in request.session):
        del request.session['connected']
        del request.session['username']
        del request.session['password']
        del request.session['trombi']
        del request.session['infos']
    logout(request)
    return http.HttpResponseRedirect('/')

#def register_view(request):
#    if request.method == 'POST':
#        form = RegisterForm(data=request.POST)
#        print ('ok')
#        if form.is_valid():
#            print('ok')
#            username = request.POST['username']
#            password = request.POST['password1']
#            form.save()
#            if login_user(request, username, password):
#                return http.HttpResponseRedirect('/')
#    else:
#        form = RegisterForm()
#    return render(request, 'auth/register.html', {'form' : form})
