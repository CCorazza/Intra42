from django.shortcuts import render

def index_view(request):
    return render(request, 'learning/index.html', {'sess' : request.session})
