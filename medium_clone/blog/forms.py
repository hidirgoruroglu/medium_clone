from django import forms
from django.core import validators
from .models import BlogPost
from tinymce.widgets import TinyMCE
from config.validators import min_length_3

class PostModelForm(forms.ModelForm):
    title = forms.CharField(validators=[min_length_3])
    tag = forms.CharField()
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 40, 'rows': 20}))
    class Meta:
        model = BlogPost
        fields = [
            'title',
            'cover_image',
            'content',
            'tag',
            'category',
        ]