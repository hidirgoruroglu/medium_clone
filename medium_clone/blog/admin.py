from django.contrib import admin
from .models import BlogPost,Category,Tag

# Register your models here.

@admin.register(BlogPost)
class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        'title',
    ]
@admin.register(Category)
class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        'title',
    ]
@admin.register(Tag)
class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        'title',
    ]