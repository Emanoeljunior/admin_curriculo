from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    summary = RichTextField()
    content = RichTextField()
    image = RichTextUploadingField()
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    date = models.DateField()
    tags = models.ManyToManyField(Tag, blank=True)
    
    def __str__(self):
        return self.title
