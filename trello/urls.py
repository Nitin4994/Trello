from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('trello/', include('user.urls')),
    path('board/', include('board.urls')),
    path('categorie/', include('categorie.urls')),
    path('task/', include('task.urls')),
]
