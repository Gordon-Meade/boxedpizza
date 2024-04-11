from django.urls import path
from .views import story

urlpatterns = [
    
    path('story/', story, name='story'),
]
