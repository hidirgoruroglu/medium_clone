from blog.models import Category

def global_categories_context(request):
    return dict(
        global_categories = Category.objects.filter(is_active = True)
    )
