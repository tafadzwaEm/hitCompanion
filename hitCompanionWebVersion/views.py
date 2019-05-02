from django.views.generic import TemplateView
from django.shortcuts import render
from collaborate.models import *


def HomePage(request):
    questions = AskQuestion.objects.all().order_by('-timestamp')
    questionsDictionary = {'questions':questions}
    return render(request,'index.html',context=questionsDictionary)

class AboutPage(TemplateView):
    template_name = 'about.html'


    

    