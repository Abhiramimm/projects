from django import forms

class EmployeeForm(forms.Form):

    name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    department=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    salary=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    location=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    email=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    address=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    dateofjoin=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))