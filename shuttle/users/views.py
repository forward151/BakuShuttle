from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views import View

from .models import User


class Register(View):

    template_name = "registration/registration.html"

    def get(self, request):
        context = {
            "form": UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        firstname = request.POST.get("username")
        secondname = request.POST.get("usersurname")
        email = request.POST.get("email")
        login_user = request.POST.get("login")
        password = request.POST.get("password")

        user = User(username=login_user, email=email, first_name=firstname, last_name=secondname)
        user.set_password(password)  # Устанавливаем пароль с использованием set_password

        user.save()

        user = authenticate(username=login_user, password=password)

        login(request, user)
        return redirect("/")
# Create your views here.
