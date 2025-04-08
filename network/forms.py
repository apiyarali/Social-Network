from django import forms
from django.forms import ModelForm
from .models import User, Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["post"]
        widgets = {
            "post" : forms.Textarea(
                attrs = {
                    "class" : "form-control text-height",
                    "rows" : "4",
                    "cols" : "10"
                }
            ) 
        }
        labels = {
            "post" : "New Post"
        }
