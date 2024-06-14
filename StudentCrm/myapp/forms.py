from django import forms

class StudentForm(forms.Form):

    name=forms.CharField()

    course=forms.CharField()

    batch=forms.IntegerField()

    duration=forms.IntegerField()

    phone_no=forms.IntegerField()