from django.contrib import admin
from django.urls import path,include

from user.views import login,register,register_save,login_success,home_page,user_loginout

urlpatterns = [
    path('', login),
    path('register/', register),
    path('register/save/', register_save),
    path('login/', login_success),
    path('home/', home_page),
    path('logout/', user_loginout),
    #path('login/', include('login.urls')),
]
