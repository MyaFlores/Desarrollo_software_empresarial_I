from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("January", views.January),
    path("February", views.February),
    path("March", views.March),
    path("April", views.April),
    path("May", views.May),
    path("June", views.June),
    path("July", views.July),
    path("August", views.August),
    path("September", views.September),
    path("October", views.October),
    path("November", views.November),
    path("December", views.December),
  
    
]


