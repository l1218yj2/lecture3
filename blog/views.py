from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    return render(request, 'index.html', context ={
        'blogs' : Blog.objects.all()
    })

def detail(reqeust, pk= None):
    return render(request, 'detail.html', context = {

    })
