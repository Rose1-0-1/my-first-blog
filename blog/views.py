from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponse
# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render (request, 'blog/post_list.html', {'posts':posts})

# def post_list(request):
#     print("Hi!")
#     return render(request, 'blog/post_list.html', {})

def hey(request):
    return HttpResponse("HEY")