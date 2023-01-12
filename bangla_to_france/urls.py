from django.urls import path
from . import views

urlpatterns = [
    
    path('vd1/', views.vida1, name='vida1'),
    path('vd2/', views.vida2, name='vida2'),
    
]
