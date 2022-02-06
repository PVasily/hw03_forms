from django.contrib.auth.views import (LogoutView, PasswordChangeView,
                                       LoginView, PasswordChangeDoneView,
                                       PasswordResetView,
                                       PasswordResetDoneView)
from django.urls import path

from . import views


app_name = 'users'


urlpatterns = [
    path('signup/', views.SugnUp.as_view(), name='signup'),
    path('login/',
         LoginView.as_view(template_name='users/login.html'),
         name='login'),
    path('logout/',
         LogoutView.as_view(template_name='users/logged_out.html'),
         name='logout'),
    path('pcf/',
         PasswordChangeView.as_view(template_name='users/pcf.html'),
         name='pcf'),
    path('pcd/',
         PasswordChangeDoneView.as_view(template_name='users/pcd.html'),
         name='pcd'),
    path('prf',
         PasswordResetView.as_view(template_name='users/prf.html'),
         name='prf'),
    path('prd/done',
         PasswordResetDoneView.as_view(template_name='users/prd.html'),
         name='prd'),
    path('send_mail/', views.mail_page, name='send_mail'),
    path('thankyou/', views.thankyou, name='thankyou')
]
