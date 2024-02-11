from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
def create(request):
    if request.method == "GET":
        return render(request, 'create.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        user = User.objects.filter(username=username).first()
        if user: # Verifica se o usuário ja existe no banco de dados
            return HttpResponse('Já existe um usuário com esse username')

        user = User.objects.create_user(username, email, password)
        print(username, password, email)
        return HttpResponse('Usuário Cadastrado com Sucesso')

def login_user(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)

            return HttpResponse('Login Feito com Sucesso')
        else:
            return HttpResponse('Usuário ou senha Inválidos')

@login_required(login_url='/user/login')    
def plataforma(request):
    return HttpResponse('Plataforma')