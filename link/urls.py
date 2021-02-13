
from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_user_send_email, name='login_user'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout_user, name='logout_user'),
    path('home/token=<str:token>', views.authenticate_user, name='authenticate_user'),
]
