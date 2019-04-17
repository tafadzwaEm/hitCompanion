from django.conf.urls import url
from .views import * 
from django.contrib.auth import views as auth_views


app_name = 'accounts'

urlpatterns = [
    url(r'^login/',auth_views.LoginView.as_view(template_name='accounts/login.html'),name='login')

]