from django.contrib import admin
from django.urls import path, include
from recipes import views


urlpatterns = [
    path('admin/', admin.site.urls),
    
]
