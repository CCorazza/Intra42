from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone

from tickets.models import Ticket, Message
from random import choice

@login_required(login_url=reverse_lazy('auth:login'))
def index_view(request):
    tickets = Ticket.objects.filter(author__id=request.user.id)
    return render(request, 'tickets/index.html', {
        'tickets' : tickets,
        'sess'    : request.session
    })

@login_required(login_url=reverse_lazy('auth:login'))
def ticket_view(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    if request.user != ticket.author and request.user != ticket.admin:
        return HttpResponseForbidden('You cannot view this ticket')
    messages = Message.objects.filter(ticket=ticket) \
                      .order_by('-pub_date')
    return render(request, 'tickets/ticket.html', {
        'ticket'   : ticket,
        'messages' : messages,
        'sess'    : request.session
    })

@staff_member_required
def spool_view(request):
    tickets = Ticket.objects.filter(admin__id=request.user.id)
    admins = User.objects.filter(is_staff=True)
    return render(request, 'tickets/spool.html', {
        'tickets' : tickets,
        'admins'  : admins,
        'sess'    : request.session
    })

@login_required
@require_POST
def post_ticket(request):
    try :
        content = request.POST['content']
        title = request.POST['ticket_title']
    except KeyError:
        return HttpResponseRedirect('/')
    admins = User.objects.filter(is_staff=True)
    try :
        admin = choice(admins)
    except IndexError:
        return HttpResponseRedirect('/')
    ticket = Ticket(
        title=title,
        admin=admin,
        author=request.user,
        pub_date=timezone.now(),
        mod_date=timezone.now()
    )
    ticket.save()
    message = Message(
        ticket=ticket,
        author=request.user,
        content=content,
        pub_date=timezone.now()
    )
    message.save()
    url = reverse('tickets:ticket', kwargs={'pk' : ticket.id})
    return HttpResponseRedirect(url)

@login_required
@require_POST
def post_message(request):
    try:
        content = request.POST['content']
        ticket_id = request.POST['ticket_id']
        next = request.POST['next']
    except KeyError:
        return HttpResponseRedirect('/')
    try:
        ticket = Ticket.objects.get(pk=ticket_id)
    except ObjectDoesNotExist:
        return HttpResponseRedirect('/')
    message = Message(
        ticket=ticket,
        author=request.user,
        content=content,
        pub_date=timezone.now()
    )
    message.save()
    ticket.mod_date = message.pub_date
    ticket.save()
    return HttpResponseRedirect(next)

@login_required
@require_POST
def post_assign(request):
    try:
        ticket_id = request.POST['ticket_id']
        admin_id = request.POST['admin_id']
        next = request.POST['next']
    except KeyError:
        return HttpResponseRedirect('/')
    try:
        admin = User.objects.get(pk=admin_id)
        ticket = Ticket.objects.get(pk=ticket_id)
    except ObjectDoesNotExist:
        return HttpResponseRedirect('/')
    if not admin.is_superuser:
        return HttpResponseRedirect('/')
    ticket.admin = admin
    ticket.mod_date = timezone.now()
    ticket.save()
    return HttpResponseRedirect(next)

@login_required
@require_POST
def post_close(request):
    try:
        ticket_id = request.POST['ticket_id']
        next = request.POST['next']
    except KeyError:
        return HttpResponseRedirect('/')
    try:
        ticket = Ticket.objects.get(pk=ticket_id)
    except ObjectDoesNotExist:
        return HttpResponseRedirect('/')
    ticket.closed = 'closed' in request.POST
    ticket.mod_date = timezone.now()
    ticket.save()
    return HttpResponseRedirect(next)
