from django.urls import path
from . import views

urlpatterns = [
    path('add/',views.add,name='add'),
    path('add_dept/<int:id>/',views.add_dept,name='addpt'),
    path('dep/',views.dep,name='dep'),
    path('grades/<int:id>/',views.grades,name='grades'),
    path('profile/<int:id>/',views.profile,name='profile'),
    path('search/',views.search,name='search'),
    path('view/<int:id>/',views.view,name='view'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
    
]