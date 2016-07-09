from django.shortcuts import render
from django.http import HttpResponse
from rangde.settings import MEDIA_ROOT, BASE_DIR
from django.http.response import HttpResponseRedirect, HttpResponse
from django.core.mail import EmailMessage
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def test(request):
    template_url = BASE_DIR + '/features/media/' + "email-template.html"
    print template_url
    content = open(template_url, "r")
    content = content.read()
    
    fr = "no-reply@rangde.com"
    to = "safwan95@gmail.com"
    
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Notification from Rangde"
    msg['From'] = fr
    msg['To'] = to
    
    part1 = MIMEText(content, 'html')
    msg.attach(part1)
    
    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    mail.login('safwan95@gmail.com', '')
    mail.sendmail('safwan95@gmail.com', 'safwan95@gmail.com', msg.as_string())
    mail.close()
    return HttpResponse("email sent")

def img(request):
    url = '/static/' + '1.gif'
    return HttpResponseRedirect(url)