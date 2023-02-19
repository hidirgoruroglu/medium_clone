from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile
from slugify import slugify
from django.contrib.auth.decorators import login_required
# Create your views here.

def login_view(request):
    context = dict()
    if request.user.is_authenticated:
        messages.info(request,"{} Zaten kayıt olmuşsunuz.".format(request.user.username))
        return redirect("home_view")
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if len(username) < 6 or len(password) < 6:
            messages.success(request,"Lütfen kullanıcı adını veya şifrenizi doğru giriniz.")
            return redirect("user_profile:login_view")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request,user)
            messages.success(request,"{} Başarıyla giriş yaptınız.".format(request.user.username))
            return redirect("home_view")
        messages.info(request,"Kullanıcı adı veya şifre yanlış.")

    return render(request,"user_profile/login.html",context)

@login_required(login_url="user:login_view")
def logout_view(request):
    messages.success(request,"Başarıyla çıkış yapıldı.")
    logout(request)
    return redirect("home_view")

def register_view(request):
    if request.method == "POST":
        post_info = request.POST
        first_name = post_info.get("first_name")
        last_name = post_info.get("last_name")
        email = post_info.get("email")
        email_confirm = post_info.get("email_confirm")
        password = post_info.get("password")
        password_confirm = post_info.get("password_confirm")
        instagram_account = post_info.get("instagram_account")
        if (len(first_name) or len(last_name) or len(password)) < 3:
            messages.warning(request,"Bilgiler en az 3 karakterden olusmalidir.")
            return redirect("user_profile:register_view")
        if email_confirm != email:
            messages.warning(request,"Lütfen email alanlarını doğru giriniz... ")
            return redirect("user_profile:register_view")
        if password_confirm != password:
            messages.warning(request,"Lütfen şifre alanlarını doğru giriniz... ")
            return redirect("user_profile:register_view")
        user , created = User.objects.get_or_create(username = email)

        if created == False:
            user_login = authenticate(request, username=email, password=password)
            if user_login:
                messages.warning(request,"Zaten daha once kayit olmussunuz... Ana sayfaya yonlendirildiniz.")
                login(request,user_login)
                return redirect("home_view")
            messages.warning(request,"{} sistemde kayitli ama giris yapmamissiniz, login sayfasina yonlendiriliyorsunuz...".format(email))
            return redirect("user_profile:login_view")
        user.email = email
        user.first_name = first_name
        user.last_name = last_name
        user.set_password(password)

        profile , profile_created = Profile.objects.get_or_create(user = user)
        profile.instagram = instagram_account
        profile.slug = slugify("{}-{}".format(user.first_name,user.last_name))
        user.save()
        profile.save()
        
        messages.success(request,"{} Başarıyla kayıt oldunuz...".format(user.first_name))
        user_login = authenticate(request, username=email, password=password)
        login(request,user_login)

        return redirect("home_view")
    context = dict()
    return render(request,"user_profile/register.html",context)