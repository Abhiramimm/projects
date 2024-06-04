from django.urls import path

from api import views

from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register("incomes",views.IncomeViewset,basename="incomes")

router.register("expenses",views.ExpenseViewset,basename="expenses") # only for viewset


urlpatterns=[

    path("register/",views.UserCreationView.as_view()),

    path("incomes/summary/",views.IncomeSummaryView.as_view()),


]+router.urls