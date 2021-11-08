"""django_app_deploy URL Configuration

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
from .math_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello', views.HelloView.as_view(), name='hello'),
    path('add/<int:num1>/<int:num2>', views.AddView.as_view(), name='add'),
    path('subtract/<int:num1>/<int:num2>', views.SubtractView.as_view(), name='subtract'),
    path('multiply/<int:num1>/<int:num2>', views.MultiplyView.as_view(), name='multiply'),
    path('divide/<int:num1>/<int:num2>', views.DivideView.as_view(), name='divide'), 
    path('modulo/<int:num1>/<int:num2>', views.ModuloView.as_view(), name='modulo'),
]
