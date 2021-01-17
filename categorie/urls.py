from django.contrib import admin
from django.urls import path,include

from categorie.views import categorie,categorie_save,categorie_delete

urlpatterns = [
    path('<int:bid>', categorie),
    path('save/', categorie_save),
    path('delete/<int:cid>', categorie_delete),

]
