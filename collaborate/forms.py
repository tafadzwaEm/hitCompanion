from django import forms
from .models import *


class AskQuestionForm(forms.ModelForm):

    class Meta():
        model = AskQuestion
        fields = ('questionTitle','questionText')

class QuestionAnswerForm(forms.ModelForm):

    class Meta():
        model = QuestionAnswer
        fields = ('answerText','questionid')
        widgets = {
            'questionid': forms.TextInput()
        }

        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            self.fields['questionid'].Label = ''
    
class FeedbackForm(forms.ModelForm):

    class Meta:
        model = Feedback
        fields = "__all__" 