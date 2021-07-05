from django.shortcuts import render, redirect
from .models import *

def root(request):
    context={
        'all_forums':Forum.objects.all()
    }
    return render(request, "forum.html", context)

def create_new_forum(request):
    print("received the request")
    #create a forum
    print(request.POST)
    new_forum=Forum.objects.create(name=request.POST['forum_name'], description=request.POST['forum_desc'])
    print(new_forum)
    return redirect('/')

def get_one_forum(request, forum_id):
    context={
        'forum': Forum.objects.get(id=forum_id)
    }
    return render(request, "one_forum.html", context)

def create_new_forum_post(request):
    new_post=Forum_Post.objects.create(content=request.POST['post_content'], username=request.POST['username'], forum=Forum.objects.get(id=int(request.POST['forum_id'])))
    print(new_post)
    return redirect(f'forum/{new_post.forum.id}')

