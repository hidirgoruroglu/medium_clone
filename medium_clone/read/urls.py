"""
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
"""

from django.urls import path

from .views import all_posts_view,post_detail_view

app_name = "read"

urlpatterns = [
    path("<slug:user_slug>/",all_posts_view,name="all_posts_view"),
    path("<slug:user_slug>/<slug:post_slug>/",post_detail_view,name="post_detail_view"),
]
