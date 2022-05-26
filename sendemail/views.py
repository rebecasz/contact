from django.shortcuts import render

# Create your views here.
# sendemail/views.py
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from .forms import ContactForm

@csrf_exempt
def contactView(request):

    subject = "Tema2"
    from_email = "llala42064@gmail.com"
    message = request.POST["text"] + '\n' + request.POST["firstname"] + '\n'+ request.POST["lastname"]
    print(request)
    try:
        send_mail(subject, message, from_email, ['szucsrebeca@gmail.com'])
    except BadHeaderError:
        return HttpResponse('Invalid header found.')
    return redirect('success')

def successView(request):
    return HttpResponse('Success! Thank you for your message.')