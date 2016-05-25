from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    return render(request, 'index.html', context ={
        'blogs' : Blog.objects.all()
    })

def detail(request, pk= None):
    return render(request, 'detail.html', context = {
        'blog' : Blog.objects.get(id=pk),
        'comments' : Comment.objects.filter(blog_id=pk),
    })
