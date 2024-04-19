from django.urls import path
from .views import dining

urlpatterns = [
    
    path('dining/', dining, name='dining'),
]