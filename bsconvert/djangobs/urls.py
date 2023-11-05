from django.urls import path
from djangobs import views


urlpatterns=[
    path('',views.index),
    path('home_msg/', views.home_msg),
    
    
]


