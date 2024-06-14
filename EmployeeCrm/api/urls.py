from django.urls import path

from api import views

urlpatterns=[

    path("employees/",views.EmployeeListCreateView.as_view()),

    path("employees/<int:pk>/",views.EmployeeRetrieveUpdateDestroyView.as_view()),

    path("employees/departments/",views.DepartmentView.as_view()),

]