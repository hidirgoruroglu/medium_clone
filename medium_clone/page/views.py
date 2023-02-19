from django.shortcuts import render
from blog.models import BlogPost, Tag, Category
# Create your views here.

def home_view(request):
    posts = BlogPost.objects.filter(is_active = True)
    top_posts = posts.order_by("-view_count")[:6]
    tags = Tag.objects.filter(is_active = True)
    categories = Category.objects.filter(is_active = True)
    context = dict(
        posts = posts,
        tags = tags,
        categories = categories,
        top_posts = top_posts,
        )
    return render(request,"page/home_page.html",context)