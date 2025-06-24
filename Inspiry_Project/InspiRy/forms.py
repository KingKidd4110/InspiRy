from django.forms import ModelForm
from .models import *
from django import forms

class postForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'post_image']
        
        
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text']
        
        
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
