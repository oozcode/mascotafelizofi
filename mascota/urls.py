from django.urls import path,include
from .import views

app_name='mascotaf'

urlpatterns = [
    path('',views.index,name='index'),
]