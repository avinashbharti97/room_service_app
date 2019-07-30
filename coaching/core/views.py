from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
# from django.template import Context, loader
# from core.forms import UserForm
# from django.contrib.auth import authenticate, login, logout
# from django.urls import reverse
# from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    return render(request, 'index.html')