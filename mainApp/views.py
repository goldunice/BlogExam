from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View
from .models import *


class MaqolalarView(View):
    def get(self, request):
        if request.user.is_authenticated:
            content = {
                "maqolalar": Maqola.objects.filter(muallif__user=request.user),
                "user": request.user.username.capitalize()
            }
        return render(request, 'main.html', content)

    def post(self, request):
        if request.user.is_authenticated:
            Maqola.objects.create(
                sarlavha=request.POST.get('sarlavha'),
                sana=request.POST.get('sana'),
                matn=request.POST.get('matn'),
                mavzu=request.POST.get('mavzu'),
                muallif=Muallif.objects.filter(user=request.user).first()
            )
            return redirect('/home/')


class MaqolaView(View):
    def get(self, request, pk):
        content = {
            'maqola': Maqola.objects.get(id=pk)
        }
        return render(request, 'maqola.html', content)


class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        User.objects.create_user(
            username=request.POST.get("username"),
            email=request.POST.get("email"),
            password=request.POST.get("password"),
        )
        return redirect('/login/')


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        user = authenticate(
            username=request.POST.get("username"),
            password=request.POST.get("password")
        )
        if user is None:
            redirect('/login/')
        login(request, user)
        return redirect('/home/')


class LogutView(View):
    def get(self, request):
        logout(request)
        return redirect('/login/')
