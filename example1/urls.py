"""
URL configuration for example1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

Url type-
slug(abc-cde)
int(1,2)
str(abc,reel)
''(when dont know the exact datatype)
"""
from django.contrib import admin
from django.urls import path,include
from example1 import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     #path('Contact/', views.contactUs),
#     path('',views.Home),
#     path('blog/',views.blog), 
#     path('contact/', views.contactUs),
#     path('courses/', views.courses),
#     path('courses/<slug:courseid>', views.coursesDetails),
# ]

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('Contact/', views.contactUs),
    path('',views.Home,name='home_Page'),
    path('blog/',views.blog), 
    path('certificate/', views.certificate),
    path('contact/', views.contact),
    path('submitdata/', views.submitdata),
    path('demo/', views.demo),
    path('userForm/', views.userForm),
]