# from anim2.account.models import Account
# from django.shortcuts import redirect, render
# # from .forms import ProfileForm, SignupForm, MyUserCreationForm
# from django.urls import reverse_lazy
# from django.views.generic import CreateView
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.views import LoginView
# from models import MyAccountManager, Account
# # from .models import Profile
# from django.contrib.auth import authenticate, login

# # Create your views here.

# class UserCreationView(CreateView):
#     form_class = Account
#     template_name = 'register.html'
#     success_url = reverse_lazy('home')


# class MyLoginView(LoginView):
#     def get(self, request, *args, **kwargs):
#         if request.user.is_authenticated:
#             return redirect('home')
#         return super().get(request, *args, **kwargs)