from django.conf.urls import url 
from .views import *
from django.urls import path

app_name = 'collaborate'

urlpatterns = [
    url('askquestion',AskQuestionPage.as_view(),name='askQuestion'),
    url('saveQuestion/',SaveQuestion),
    path('comment/<int:id>/',AnswerQuestionPage),
    path('saveAnswer/<int:id>/',SaveAnswer),
]