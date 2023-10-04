from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('hello/', views.say_hello),
    path('send-attachment/', views.send_attachment),
    path('check-celery/', views.check_celery),
]
