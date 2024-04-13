from django.shortcuts import render, redirect
from django.views import View
from .forms import RegisterForm, LoginForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, "users/register.html", {"form": form})

    def post(self, request):
        context = {}
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get("username")
            messages.success(request, f"'{name}' you succesffully registered 😁👍")
            return redirect('musiks:home')
        context['form'] = form
        messages.warning(request, "Your authentification are not validation 😥😣😵!")
        return render(request, "users:register", context)


class LogoutView(View):
    def get(self, request):
        return render(request, "users/logout.html")

    def post(self, request):
        logout(request)
        return redirect("musiks:home")


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, "users/login.html", {"form": form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request = request, user = user)
                messages.success(request, f"'{username}' yor are logged 😃😎😉")
            else:
                messages.warning(request, "Invalid username or password ! ☹️😞")
                return redirect(request, "users/login.html", {"form": form})
        messages.warning(request, "Validation error in logged ! 😞")
        return render(request, "users/login.html", {"form": form})
