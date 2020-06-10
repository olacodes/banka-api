"""banka URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include, re_path
from .views import (notfound, index, home)


urlpatterns = [
    # match api index route request
    re_path(r'^(?:api/v1?)$', index),

    # match api/v1 routes
    path('api/v1/', include('api.urls')),

    # match all other routes and respond with 403
    re_path(r'^(?:.*)$', home)
]
