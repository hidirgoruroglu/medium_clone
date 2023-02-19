from django.shortcuts import render,get_object_or_404

from user_profile.models import Profile
from blog.models import BlogPost
# Create your views here.

def all_posts_view(request, user_slug):
    profile = get_object_or_404(Profile, slug = user_slug)
    posts = BlogPost.objects.filter(user = profile.user, is_active = True)

    context = dict(
        posts = posts,
        profile = profile,
    )
    return render(request,"read/all_posts.html",context)

def post_detail_view(request,user_slug,post_slug):
    post = get_object_or_404(BlogPost,slug = post_slug,is_active = True)
    post.view_count += 1
    post.save()
    context = dict(
        post = post,
    )
    return render(request,"read/post_detail.html",context)
