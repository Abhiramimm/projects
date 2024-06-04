from django.shortcuts import render

from rest_framework.response import Response

from rest_framework.views import APIView

from rest_framework import viewsets

from rest_framework import authentication,permissions

from api.serializers import UserSerializer

from api.serializers import ExpenseSerializer,Incomeserializer

from api.permissions import OwnerOnly

from django.contrib.auth.models import User

from django.db.models import Sum

from django.utils import timezone

from budget.models import Expense,Income


# Create your views here.


class UserCreationView(APIView):

    def post(self,request,*args,**kwargs):
 
        serializer_instance=UserSerializer(data=request.data)  #deserialization

        if serializer_instance.is_valid():

            # data=serializer_instance.validated_data

            # User.objects.create_super(**data)

            serializer_instance.save()

            return Response(data=serializer_instance.data)
        
        else:

            return Response(data=serializer_instance.errors)

class ExpenseViewset(viewsets.ModelViewSet):

    serializer_class=ExpenseSerializer

    queryset=Expense.objects.all()

    authentication_classes=[authentication.BasicAuthentication]

    permission_classes=[permissions.IsAuthenticated]
    
class IncomeViewset(viewsets.ModelViewSet):

    serializer_class=Incomeserializer

    queryset=Income.objects.all()

    authentication_classes=[authentication.BasicAuthentication]

    permission_classes=[OwnerOnly]

    def list(self,request,*args,**kwargs):

        qs=Income.objects.filter(user_object=request.user)

        serializer_instance=Incomeserializer(qs,many=True)

        return Response(data=serializer_instance.data)
    
    def perform_create(self,serializer):

        serializer.save(user_object=self.request.user)

class IncomeSummaryView(APIView):

    permission_classes=[permissions.IsAuthenticated]

    authentication_classes=[authentication.BasicAuthentication]

    def get(self,request,*args,**kwargs):

        current_month=timezone.now().month

        current_year=timezone.now().year

        all_incomes=Income.objects.filter(

            user_object=request.user,

            created_date__month=current_month,

            created_date__year=current_year

            )
        
        income_total=all_incomes.values("amount").aggregate(total=Sum("amount"))["total"]

        print(income_total)

        category_summary=all_incomes.values("category").annotate(total=Sum("amount"))

        print(category_summary)


        data={

            "income_total":income_total,

            "category_summary":category_summary,    
        }

        return Response(data=data)

        