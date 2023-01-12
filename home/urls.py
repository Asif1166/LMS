from django.urls import path
from . import views

urlpatterns = [
    path('ab/', views.about, name='about'),
    path('cr/', views.course, name='course'),
    path('ct/', views.contact, name='contact'),
    path('tc/', views.teacher, name='teacher'),
    path('ex/', views.exam, name='exam'),
    path('lb/', views.library, name='library'),
    
    path('login', views.LoginView.as_view(), name='login'),
    path('signup2', views.signup2, name='signup2'),
    path('logout', views.signout, name='logout'),
    path('fcl/', views.f_culture, name='f_culture'),
    path('bcl/', views.b_culture, name='b_culture'),
    path('gl/', views.gallery, name='gallery'),
    path('brd/', views.board, name='board'),
    path('live/', views.LiveClass, name='live_class'),
    
    
]