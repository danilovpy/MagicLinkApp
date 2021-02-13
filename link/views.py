from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
from .utils import get_random_string, send_magic_link
from .models import User
from django.core.mail import send_mail


def create_user_send_email(request):
    form = CreateUserForm()
    message = None
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        user = form.save(commit=False)
        if form.is_valid():
            if not User.objects.filter(email=request.POST.get("email")):
                user.token = get_random_string()
                user.username = get_random_string()
                user.save()
            user = User.objects.get(email=user.email)
            message = f"An email has been sent to {user.email}"
            send_magic_link(request, user.email, user.token)
    print(request.get_host())
    return render(request, "link/login.html", {'form': form, 'message': message})


@login_required(login_url='login')
def home(request):
    email = request.user
    count = request.user.count
    return render(request, "link/home.html", {'email': email, 'count': count})


def authenticate_user(request, token):
    if User.objects.filter(token=token):
        user = User.objects.get(token=token)
        user.count += 1
        user.save()
        login(request, user)
        return redirect('home')
    return redirect('login_user')


def logout_user(request):
    logout(request)
    return redirect('login_user')