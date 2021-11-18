"""NewProject URL Configuration

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
from django.urls import path
from crud.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", log_in, name="login_page"),
    path("index/", index, name="index"),
    path('register/', register, name='register'),
    path('home/', home, name='home'),
    path('delete/<int:id>', delete, name='delete'),
    path('edit/<int:id>', edit, name='edit'),
    path('forgot_password/', forgot_password, name="forgot_password"),
    path('gallery/', gallery, name='gallery'),
    path('members/', members, name='members')
]
