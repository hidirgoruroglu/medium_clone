"""
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
"""
from django.urls import path

from .views import create_blog_post_view,tag_view,category_view


app_name = "blog"

urlpatterns = [
    path('create/',create_blog_post_view,name='create_blog_post_view'),
    path('tag/<slug:tag_slug>/',tag_view,name='tag_view'),
    path('category/<slug:category_slug>/',category_view,name='category_view'),
]