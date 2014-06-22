from copy import copy
from modules.models import Module
from modules.models import Activity
from modules.models import RegisteredModule
from modules.models import RegisteredActivity
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

def list_modules(request):
  return render(request, 'modules/index.html', {'sess' : request.session})

def module_descr(request, module):
  if ('connected' in request.session):
    sess = request.session
    registered = False
    module = Module.objects.filter(uid=module)
    if (module):
      module = module[0]
      if (RegisteredModule.objects.filter(username=sess['username'], module=module.uid)):
        registered = True
      members = RegisteredModule.objects.filter(module=module.uid)
      registered_nb = len(members)
      del members
      j = {}
      activities = []
      activity = Activity.objects.filter(belongs=module.uid)
      for i in activity:
        j['name'] = i.name
        j['registered'] = False
        if (RegisteredActivity.objects.filter(username=sess['username'], activity=i.uid)):
          j['registered'] = True
        activities.append(copy(j))
    return render(request, 'modules/module.html', locals())
  else:
    return redirect('/login')
