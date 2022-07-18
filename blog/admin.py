from django.contrib import admin

# Register your models here.
from blog.models import Post, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    model = Post


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    model = Tag
