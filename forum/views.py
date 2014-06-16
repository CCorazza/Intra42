from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse

from forum.models import Category, Thread, Message, Comment

def index_view(request):
    categories = Category.objects.filter(parent_category__isnull=True)
    return render(request, 'forum/index.html', {
        'categories' : categories
    })

def category_view(request, pk):
    category = get_object_or_404(Category, pk=pk)
    sub_categories = Category.objects.filter(parent_category=category)
    threads = Thread.objects.filter(category=category) \
                            .order_by('pub_date')
    return render(request, 'forum/categories.html', {
        'category'       : category,
        'sub_categories' : sub_categories,
        'threads'        : threads
    })

def thread_view(request, pk):
    thread = get_object_or_404(Thread, pk=pk)
    messages = Message.objects.filter(thread=thread) \
                              .order_by('pub_date')
    comments = Comment.objects.filter(message__in=messages)
    posts = list()
    for message in messages :
        posts.append((
            message,
            comments.filter(message=message).order_by('pub_date')
        ))
    return render(request, 'forum/thread.html', {
        'thread'   : thread,
        'posts'    : posts
    })

@login_required
@require_POST
def post_reply(request):
    try:
        content = request.POST['content']
        thread_id = request.POST['thread_id']
        next = request.POST['next']
    except KeyError:
        return HttpResponseRedirect('/')
    try :
        thread = Thread.objects.get(pk=thread_id)
    except ObjectDoesNotExist:
        return HttpResponseRedirect('/')
    message = Message(
        thread=thread,
        author=request.user.username,
        content=content,
        pub_date=timezone.now()
    )
    message.save()
    return HttpResponseRedirect(next)

@login_required
@require_POST
def post_comment(request):
    try:
        content = request.POST['content']
        message_id = request.POST['message_id']
        next = request.POST['next']
    except KeyError:
        return HttpResponseRedirect('/')
    try:
        message = Message.objects.get(pk=message_id)
    except ObjectDoesNotExist:
        return HttpResponseRedirect('/')
    comment = Comment(
        message=message,
        author=request.user.username,
        content=content,
        pub_date=timezone.now()
    )
    comment.save()
    return HttpResponseRedirect(next)

@login_required
@require_POST
def post_thread(request):
    try:
        content = request.POST['content']
        category_id = request.POST['category_id']
        thread_title = request.POST['thread_title']
    except KeyError:
        return HttpResponseRedirect('/')
    try:
        category = Category.objects.get(pk=category_id)
    except ObjectDoesNotExist:
        return HttpResponseRedirect('/')
    thread = Thread(
        title=thread_title,
        category=category,
        author=request.user.username,
        pub_date=timezone.now()
    )
    thread.save()
    message = Message(
        thread=thread,
        author=request.user.username,
        content=content,
        pub_date=timezone.now()
    )
    message.save()
    url = reverse('forum:thread', kwargs={'pk' : thread.id})
    return HttpResponseRedirect(url)
