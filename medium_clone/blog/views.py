from django.shortcuts import render,redirect,get_object_or_404
from .forms import PostModelForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Tag,Category,BlogPost
import json
# from .models import Category,Tag,BlogPost

# Create your views here.
@login_required(login_url='user:login_view')
def create_blog_post_view(request):
    form = PostModelForm()
   
    if request.method == "POST":
        form = PostModelForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()
            tags = json.loads(form.cleaned_data.get('tag'))
            for tag in tags:
                tag_item, created = Tag.objects.get_or_create(title = tag.get('value').lower())
                tag_item.is_active = True
                tag_item.save()
                f.tag.add(tag_item)
            messages.success(request,"Blog başarıyla eklendi.")
            return redirect("blog:create_blog_post_view")
    context = dict(
        form = form,
    )
    return render(request,"blog/create_blog_post.html",context)

def category_view(request,category_slug):
    category = get_object_or_404(Category, slug = category_slug)
    posts = BlogPost.objects.filter(category = category,is_active = True)
    context = dict(
        posts = posts,
        category = category,
    )
    return render(request,"blog/post_list.html",context)

def tag_view(request,tag_slug):
    tag = get_object_or_404(Tag, slug = tag_slug)
    posts = BlogPost.objects.filter(tag = tag)
    context = dict(
        posts = posts,
        tag = tag,
    )
    return render(request,"blog/post_list.html",context)