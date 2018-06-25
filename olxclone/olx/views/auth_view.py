from django.views import View
from django.shortcuts import render, redirect
from olx.forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages



def sample(request):
    return render(request,'olx/sample.html',{})




class SignUpView(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            form = SignUpForm
            return render(
                request,
                'olx/signup.html',
                {'form': form, 'title': 'Signup|TODO list'}
            )
        else:
            return redirect('olx:sample')

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(**form.cleaned_data)
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )

            if user is not None:
                login(request, user)
                return redirect('olx:sample')
            else:
                messages.error(request, "Invalid Credentials!!!")

            return render(
                request,
                'olx/signup.html',
                {'form': form}
            )


class LoginView(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            form = LoginForm
            return render(
                request,
                'olx/login.html',
                {'form': form, 'title': 'Login|OLXClone'}
            )
        else:
            return redirect('olx:sample')

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            # user=User.objects.create_user(**form.cleaned_data)
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )

            if user is not None:
                login(request, user)
                return redirect('olx:sample')
            else:
                messages.error(request, "Invalid Credentials!!!")

            return render(
                request,
                'olx/signup.html',
                {'form': SignUpForm}
            )


def logout_user(request):
    logout(request)
    return redirect('olx:login')


