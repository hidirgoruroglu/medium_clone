from django.db import models

# Create your models here.
from django.db import models

from django.contrib.auth.models import User

#Third party apps
from autoslug import AutoSlugField
from django.urls import reverse
from tinymce import models as tinymce_models
# Create your models here.

class CommonModel(models.Model):
    title = models.CharField(max_length=30)
    slug = AutoSlugField(populate_from = 'title',unique=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
        ordering = ("title",)



class Category(CommonModel):
    
    
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("blog:category_view", kwargs={"category_slug": self.slug})


class Tag(CommonModel):

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("blog:tag_view", kwargs={"tag_slug": self.slug})


class BlogPost(CommonModel):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    tag = models.ManyToManyField(Tag)
    cover_image = models.ImageField(upload_to='post')
    content = tinymce_models.HTMLField(blank=True,null=True) # doldurmak zorunda değiliz.
    view_count = models.BigIntegerField(default=0)

    def __str__(self):
        return self.title
    class Meta:
        ordering = ("-created_at",)
    def get_absolute_url(self):
        return reverse("read:post_detail_view", kwargs={"user_slug": self.user.profile.slug,"post_slug": self.slug})