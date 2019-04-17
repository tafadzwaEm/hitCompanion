from django.views.generic import ListView
from django.shortcuts import render
from collaborate.models import *


def HomePage(request):
    questions = AskQuestion.objects.all().order_by('-timestamp')
    questionsDictionary = {'questions':questions}
    return render(request,'index.html',context=questionsDictionary)


    

    