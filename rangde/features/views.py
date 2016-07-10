from django.shortcuts import render
from django.http import HttpResponse
from rangde.settings import MEDIA_ROOT, BASE_DIR
from django.http.response import HttpResponseRedirect, HttpResponse
from django.core.mail import EmailMessage
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#from twilio.rest import TwilioRestClient


def sendsms(request):
    account_sid = "AC549130b8beb5998efd169d5ab4e3ff8f"
    auth_token  = "8cbaefc7e7f16ae6a636a3a5c2bd0d1d"
    client = TwilioRestClient(account_sid, auth_token)
    
    message = client.messages.create(
        body="Notification from Rangde",
        to="+919008384564",
        from_="+13345641349",     
        media_url="https://rangde-org-gen.s3-ap-southeast-1.amazonaws.com/images/logos/logo_with_black_text.png")
    print message.sid       
    
    return HttpResponse('sent!')

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
