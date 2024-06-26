"""boxedpizza URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from home.views import index  
from bookings import views as bookings_views 
from story import views as story_views 
from menu.views import menu

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('', index, name='index'), 
    path('home/', include('home.urls')),
    path('booking/', include('bookings.urls')),
    path('story/', include('story.urls')),
    path('dining/', include('dining.urls')),
    path('menu/', include('menu.urls')),
    path('retail/', include('retail.urls')),
]




