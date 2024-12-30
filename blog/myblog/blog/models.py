from django.db import models
from django.conf import settings
from django_ckeditor_5.fields import CKEditor5Field


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = CKEditor5Field('content')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
