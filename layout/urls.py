from django.urls import path
from . import views

urlpatterns = [
    path('lay/', views.layout, name='layout'),
    path('signup/', views.signup, name='signup' ),
    path('signin/', views.signin, name='signin' ),
    path('signout/', views.signout, name='signout' ),
    path('contact/', views.contact, name='contact' ),
]

