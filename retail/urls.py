from django.urls import path
from .views import retail

urlpatterns = [
    
    path('retail/', retail, name='retail'),
]
