from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail, mail_admins, BadHeaderError, EmailMessage, EmailMultiAlternatives
from .tasks import notify_customers



def say_hello(request):
    try: 
        send_mail('subject', 'message', 'cinortcele1@gmail.com', ['a.aslani1986@gmail.com', ])
    except BadHeaderError:
        return HttpResponse('Invalid header found.')
    return HttpResponse('Success! Your email has been sent.')


def send_attachment(request):
    try:
        message = EmailMessage('subject', 'message', 'cinortcele1@gmail.com', ['a.aslani1986@gmail.com', ])
        message.attach_file('playground/static/images/1.JPG')
        message.send()
        return HttpResponse('Success! Your email has been sent.')
    except BadHeaderError:
        return HttpResponse('Invalid header found.')



def check_celery(request):
    notify_customers.delay('Hello')
    return HttpResponse('Celery is working!')
