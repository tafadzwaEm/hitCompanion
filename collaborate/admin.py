from django.contrib import admin
from .models import *

admin.site.register(Feedback)
admin.site.register(AskQuestion)
admin.site.register(QuestionAnswer)

# Register your models here.
