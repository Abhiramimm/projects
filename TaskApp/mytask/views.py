from django.shortcuts import render,redirect

from django.views.generic import View

from mytask.forms import TaskForm,RegistrationForm,LoginForm

from mytask.models import Task

from django.contrib import messages

from django.utils import timezone

from django.db.models import Count

from django.contrib.auth.models import User

from django.contrib.auth import authenticate,login,logout

from mytask.decorators import signin_required

from django.utils.decorators import method_decorator




# from django.db.models.functions import ExtractMonth

# Create your views here.


@method_decorator(signin_required,name="dispatch")
class TaskCreateView(View):

    def get(self,request,*args,**kwargs):

        form_instance=TaskForm()

        qs=Task.objects.filter(user_object=request.user).order_by("-created_date")

        return render(request,"task_add.html",{"form":form_instance,"data":qs})
    
    def post(self,request,*args,**kwargs):

        form_instance=TaskForm(request.POST)

        if form_instance.is_valid():

            # form_instance.save()

            data=form_instance.cleaned_data

            Task.objects.create(**data,user_object=request.user)

            messages.success(request,"created successfully!!!")

            # print("task object has been created")

            return redirect("task-add")
        
        else:

            messages.error(request,"An error occured!!!")

            return render(request,"task_add.html",{"form":form_instance})
        

@method_decorator(signin_required,name="dispatch")       
class TaskUpdateView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        task_object=Task.objects.get(id=id)

        form_instance=TaskForm(instance=task_object)

        return render(request,"task_edit.html",{"form":form_instance})
    

    def post(self,request,*args,**kwrags):

        id=kwrags.get("pk")

        task_object=Task.objects.get(id=id)

        form_instance=TaskForm(instance=task_object,data=request.POST)

        if form_instance.is_valid():

            form_instance.save()

            messages.success(request,"Updated successfully!!!")

            return redirect("task-add")
        
        else:
            messages.error(request,"Failed to update!!!")
            
            return render(request,"task_edit.html",{"form":form_instance})


@method_decorator(signin_required,name="dispatch")
class TaskDetailView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        qs=Task.objects.get(id=id)

        return render(request,"task_detail.html",{"data":qs})


@method_decorator(signin_required,name="dispatch")
class TaskDeleteView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        Task.objects.get(id=id).delete()

        messages.success(request,"deleted successfully!!!")

        return redirect("task-add")


@method_decorator(signin_required,name="dispatch")
class TaskSummaryView(View):

    def get(self,request,*args,**kwargs):

        current_month=timezone.now().month

        current_year=timezone.now().year

        task_list=Task.objects.filter(
            
                                        user_object=request.user,

                                        created_date__month=current_month,

                                        created_date__year=current_year,

                                    )
        

        # task_summary=task_list.annotate(count=Count("status"))

        # print("task_summary***",task_summary)

        true_count=Task.objects.filter(user_object=request.user,status=True).count()

        print("false:****",true_count)

        false_count=Task.objects.filter(user_object=request.user,status=False).count()
        
        print("True:****",false_count)


        # total_tasks = task_list.all().count()

        total_tasks=true_count + false_count

        print("total task*****",total_tasks)

        
        

        

        print("hello there")

        return render(request,"task_summary.html",{
            # "task_summary":task_summary,
            "true_count":true_count,
            "false_count":false_count,
            "total_tasks":total_tasks
        })


class SignUpView(View):

    def get(self,request,*args,**kwargs):

        form_instance=RegistrationForm()

        return render(request,"register.html",{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_instance=RegistrationForm(request.POST)

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            User.objects.create_user(**data)

            print("user created")

            return redirect("signin")
        
        else:

            return redirect("register") 


class SigInView(View):

    def get(self,request,*args,**kwargs):

        form_instance=LoginForm()

        return render(request,"login.html",{"form":form_instance})
    
    
    def post(self,request,*args,**kwargs):

        form_instance=LoginForm(request.POST)

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            uname=data.get("username")

            pwd=data.get("password")

            print(uname,pwd)

            user_object=authenticate(request,username=uname,password=pwd)

            print(user_object)

            if user_object:

                login(request,user_object)
            
                return redirect("task-add")
        
        messages.error(request,"invalid credentials")

        return render(request,"login.html",{"form":form_instance})
 
    
@method_decorator(signin_required,name="dispatch")
class SignOutView(View):

    def get(self,request,*args,**kwargs):

        logout(request)

        return redirect("signin")



        

    


            






