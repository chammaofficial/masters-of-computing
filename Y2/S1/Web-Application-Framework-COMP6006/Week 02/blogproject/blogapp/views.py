from django.shortcuts import render
from django.http import HttpResponse

from blogapp.models import Post


# Create your views here.

def index(request):
    postsQuerySet = Post.objects.all()
    return render(request,'index.html',{'posts':postsQuerySet})

