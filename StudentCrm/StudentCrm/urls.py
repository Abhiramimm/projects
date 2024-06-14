"""
URL configuration for StudentCrm project.

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
"""
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('students/all/',views.StudentListView.as_view(),name="student-list"),

    path('students/add/',views.StudentCreateView.as_view(),name="student-create"),

    path('students/<int:pk>/',views.StudentDetailView.as_view(),name="student-detail"),

    path('students/<int:pk>/delete/',views.StudentDeleteView.as_view(),name="student-delete"),

    path('students/<int:pk>/change/',views.StudentUpdateView.as_view(),name="student-edit"),
]
