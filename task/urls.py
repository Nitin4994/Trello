from django.contrib import admin
from django.urls import path,include

#from categorie.views import categorie,categorie_save
from task.views import task_save,task_delete,task_move

urlpatterns = [
    path('save/', task_save),
    path('delete/<int:tid>', task_delete),
    path('move/', task_move),

]
