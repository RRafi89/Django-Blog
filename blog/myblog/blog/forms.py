from django import forms
from .models import Post
from django_ckeditor_5.widgets import CKEditor5Widget

class EditForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditor5Widget())
    class Meta:
        model = Post
        fields = ["title", "content"]
