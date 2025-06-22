from django.forms import ModelForm
from .models import *

class postForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'post_image']
        
        
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text']
