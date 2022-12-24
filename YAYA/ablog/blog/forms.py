from django import forms
from .models import Post, Comment
from django.forms import ModelForm

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "author", "body")

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "author": forms.TextInput(attrs={"class": "form-control", "value":"", "id":"elder", "type":"hidden"}),
            #"author": forms.Select(attrs={"class": "form-control"}),
            "body": forms.Textarea(attrs={"class": "form-control"}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "body")

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "body": forms.Textarea(attrs={"class": "form-control"}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("author", "body")

        widgets = {
            "author": forms.TextInput(attrs={"class": "form-control", "value":"", "id":"elderdragon", "type":"hidden"}),
            "body": forms.Textarea(attrs={"class": "form-control"}),
        }
