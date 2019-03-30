"""tutoriel_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import  handler404, handler500, url
from django.conf import settings


from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('create', views.contact, name='contact'),
    path('blog/', include('blog.urls')),
    path('admin/', admin.site.urls)
]

handler404 = 'tutoriel_django.views.handler404'
handler505 = 'tutoriel_django.views.handler500'

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns