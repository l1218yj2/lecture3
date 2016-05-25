from django.shortcuts import render
from .models import *
from .forms import *
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, 'index.html', context ={
        'blogs' : Blog.objects.all()
    })

def detail(request, pk= None):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            Comment.objects.create(blog=Blog.objects.get(id=pk), content = content)
            messages.success(request, "Huge success!")
        else:
            messages.error(request, "fail")

    form = CommentForm()
    return render(request, 'detail.html', context={

        'blog':Blog.objects.get(id=pk),
        'comments':Comment.objects.filter(blog__id=pk),
        'form':form,

    })
