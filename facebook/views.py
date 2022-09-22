from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


def login(request):
    return render(request, 'registration/login.html')


# class HomeView(LoginRequiredMixin, TemplateView):
#     template_name = "home.html"

@login_required
def home(request):
    return render(request, 'home.html')
