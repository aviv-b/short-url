"""shorturl URL Configuration
"""
from django.contrib import admin
from django.urls import path,include
from apps.urls import views as urls_view
urlpatterns = [
    path('', urls_view.main ,name = 'main'),
    path('create/', urls_view.create ,name = 'create'),
    path('s/<str:short_url>', urls_view.short_url,name='get'),
    
    path('api/', include('api.urls'), name='api')
]
