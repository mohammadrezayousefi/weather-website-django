from django.contrib import admin
from django.urls import path , include
from .views import weather


urlpatterns = [
    path('' ,weather , name = 'home' )
]