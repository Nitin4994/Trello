from django.contrib import admin
from django.urls import path,include

#from user.views import login,register,register_save,login_success,home_page,user_loginout
from board.views import board,board_save,board_delete

urlpatterns = [
    path('', board),
    path('save/', board_save),
    path('delete/<int:bid>', board_delete),

]
