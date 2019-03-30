from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.core.paginator import Paginator

#from .mocks import Post
from . models import Post

def index(request):
  
     paginator = Paginator(Post.objects.all(), 6)
     page = request.GET.get('page')
     posts = paginator.get_page(page)

     return render(request, 'blog/index.html',{'posts':posts})

def show(request, id):
    post = get_object_or_404(Post, pk=id)
    
    #try:
     #   post = Post.objects.get(pk=id)
    #except Post.DoesNoExist:
    #    raise Http404("Oups ! pas de post #{} retouvé".format(id))

    return render(request, 'blog/show.html', {'post':post})