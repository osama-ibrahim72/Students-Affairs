from django.urls import path
from . import views

urlpatterns = [
    path('',views.prepage,name='prepage'),
    path('home/',views.index,name='index')
]