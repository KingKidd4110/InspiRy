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
    


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture', 'bio', 'birthday', 'social_link']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add Tailwind classes to all fields
        for field_name, field in self.fields.items():
            if field_name != 'profile_picture':  # We'll handle this separately
                field.widget.attrs.update({
                    'class': 'w-full px-3 py-2 bg-gray-700 border border-gray-600 rounded-md text-gray-200 focus:outline-none focus:ring-2 focus:ring-blue-500'
                })
        
        # Special handling for profile picture
        self.fields['profile_picture'].widget.attrs.update({
            'class': 'hidden'  # We'll handle this with custom JavaScript
        })
