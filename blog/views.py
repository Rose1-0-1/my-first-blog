from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponse
# Create your views here.

def post_list(request):
    print("Hi!")
    return render(request, 'blog/post_list.html', {})
def hey(request):
    return HttpResponse("HEY")