from django.shortcuts import render
from django.shortcuts import redirect

def home(request):
  if ('connected' in request.session):
    return render(request, "intra/index.html", {'sess': request.session})
  else:
    return redirect('/login')
