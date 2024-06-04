from django import forms
from myapp.models import Movie

class MovieForm(forms.Form):

    title=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control border border-danger"}))

    year=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control border border-danger"}))

    director=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control border border-danger"}))

    run_time=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control border border-danger"}))

    language=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control border border-danger"}))

    genre=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control border border-danger"}))

    producer=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control border border-danger"}))



class MovieModelForm(forms.ModelForm):

    class Meta:

        model=Movie

        exclude=("id",)

        widgets={

            "title":forms.TextInput(attrs={"class":"form-control"}),

            "year":forms.TextInput(attrs={"class":"form-control"}),

            "run_time":forms.NumberInput(attrs={"class":"form-control"}),

            "language":forms.TextInput(attrs={"class":"form-control"}),

            "director":forms.TextInput(attrs={"class":"form-control"}),

            "genre":forms.TextInput(attrs={"class":"form-control"}),

            "producer":forms.TextInput(attrs={"class":"form-control"})
        }