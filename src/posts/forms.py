from django import forms
from easy_thumbnails.widgets import ImageClearableFileInput
from tinymce.widgets import TinyMCE

from .models import Post


class PostForm(forms.ModelForm):
    image = forms.ImageField(widget=ImageClearableFileInput())
    content = forms.CharField(widget=TinyMCE())

    class Meta:
        model = Post
        fields = ['image', 'title', 'description', 'content', 'author']
        widgets = {'author': forms.HiddenInput}
