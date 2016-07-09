from django.shortcuts import render
from django.http import HttpResponse
from rangde.settings import MEDIA_ROOT
from django.http.response import HttpResponseRedirect

def test(request):
    return HttpResponse("This is a sample success story - Sample Sample Sample Sample")

def img(request):
    url = '/static/' + '1.gif'
    return HttpResponseRedirect(url)