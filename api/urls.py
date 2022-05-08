from django.urls import path 
from . import views

urlpatterns = [
    path('all/', views.get_all),
    path('create/', views.create),
    path('s/<str:short>', views.get),
    path('get/<str:short>', views.get_one),
]

