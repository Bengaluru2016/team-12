from django.shortcuts import render
from django.http.response import HttpResponse
from features.models import seek_info_table

def home_page(request):
    return render(request, "index.html", {})

def seek_info(request):
    if request.POST:
        visitor_name = request.POST.get('name')
        email = request.POST.get('email')
        mobile= request.POST.get('mobile')
        question = request.POST.get('question')
        
        return HttpResponse("hello")