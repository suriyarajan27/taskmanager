from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from currentmood .models import *


def signup(request):
    if request.method == 'POST':
        fnm = request.POST.get('fnm')
        email = request.POST.get('email')
        pwd = request.POST.get('pwd')
        print(fnm, email, pwd)
        my_user = SignUpList.objects.create(
            username = fnm, email = email, password = pwd
        )
        my_user.save()
        return redirect('/loginn')
    return render(request, 'signup.html')

def loginn(request):
    if request.method == 'POST':
        fnm = request.POST.get('fnm')
        pwd = request.POST.get('pwd')
        print(fnm, pwd)
        m_user = LoginUpList.objects.create(
            username = fnm, password = pwd
        )
        m_user.save()
    return render(request, 'loginn.html')

def todo(request):
    return render(request, 'todo.html')
