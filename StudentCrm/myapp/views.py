from django.shortcuts import render,redirect
from django.views.generic import View
from myapp.models import Student
from myapp.forms import StudentForm

# Create your views here.

class StudentListView(View):

    def get(self,request,*args,**kwargs):

        qs=Student.objects.all()

        return render(request,"student_list.html",{"data":qs})


class StudentCreateView(View):

    def get(self,request,*args,**kwargs):

        form_instance=StudentForm()

        return render(request,"student_add.html",{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_instance=StudentForm(request.POST)

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            Student.objects.create(**data)

            return redirect("student-list")
        else:

            return render(request,"student_add.html",{"form":form_instance})

class StudentDetailView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        qs=Student.objects.get(id=id)

        return render(request,"student_detail.html",{"data":qs})

class StudentDeleteView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        Student.objects.get(id=id).delete()

        return redirect("student-list")

class StudentUpdateView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        student_object=Student.objects.get(id=id)

        dictionary={
            "name":student_object.name,
            "course":student_object.course,
            "batch":student_object.batch,
            "duration":student_object.duration,
            "phone_no":student_object.phone_no

        }

        form_instance=StudentForm(initial=dictionary)

        return render(request,"student_edit.html",{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_instance=StudentForm(request.POST)
        
        id=kwargs.get("pk")


        if form_instance.is_valid():

            data=form_instance.cleaned_data

            Student.objects.filter(id=id).update(**data)

            return redirect("student-list")
            

