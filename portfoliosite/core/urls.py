from django.urls import path
from .views import *
from core import views

urlpatterns = [
    path('', LandingTemplateView.as_view()),
    path('contact/send/',views.create_send_mail),
]