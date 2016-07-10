from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from features.models import seek_info_table, refer_info_table

def home_page(request):
    return render(request, "index.html", {})

def seek_info(request):
    if request.POST:
        visitor_name = request.POST.get('visitor_name')
        email = request.POST.get('email')
        mobile= request.POST.get('mobile')
        question = request.POST.get('question')
    
        
        seek_info_table.objects.create(visitor_name=visitor_name,
                                       mobile_number=mobile,
                                       email_id=email,
                                       question=question)
        
    return HttpResponseRedirect("/home/")

def refer_info(request):
    if request.POST:
        referrer_name = request.POST.get('referrer_name')
        referred_name = request.POST.get('referred_name')
        email_id = request.POST.get('email')
        mobile_number = request.POST.get('mobile')
        
        refer_info_table.objects.create(referrer_name=referrer_name,
                                        referred_name=referred_name,
                                        email_id=email_id,
                                        mobile_number=mobile_number,
                                        )
    return HttpResponseRedirect("/home/")

def rangde_admin(request):
    return render(request, "admin.html", {})

def queries(request):
    qs = seek_info_table.objects.all()

    return render(request, "queries.html", {'qs' : qs})