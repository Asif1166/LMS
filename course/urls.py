from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('courses/<str:slug>', views.CoursePage, name='coursepage'),
    path('enroll/<str:slug>', views.Enroll, name='enroll'),
]