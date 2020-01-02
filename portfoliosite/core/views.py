from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import *
from django.http import HttpResponse
from django.core import mail
from django.conf import settings
from django.core.mail import EmailMultiAlternatives

class LandingTemplateView(TemplateView):
    template_name = 'landingpage.html'

    # override get context data method
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # call super to get context data
        context['about'] = About.objects.first()
        context['skills'] = Skill.objects.all()
        context['projects'] = CompletedProject.objects.all()
        context['clients'] = Client.objects.all()
        return context



def create_send_mail(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        mail = EmailMultiAlternatives(name + " " + email,message,email,['asif000473@gmail.com'])
        mail.send()

        Contact.objects.create(
            fullname = name,
            email = email,
            message = message,
        )



        return HttpResponse('')


    
