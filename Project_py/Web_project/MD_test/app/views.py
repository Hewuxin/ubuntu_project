from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponse("index")


def sendemail(request):
    subject = "EMAIL test"
    message = "<h1>Hello</h1>  <a>www.baidu.com</a>"
    from_email = "py_daxinzang@163.com"
    recipient_list = ["py_daxinzang@163.com"]
    send_mail(subject=subject, message=message, from_email=from_email, recipient_list=recipient_list,
              html_message=message)

    return HttpResponse("send success")
