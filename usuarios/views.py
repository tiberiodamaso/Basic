from django.contrib import auth, messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from usuarios.models import Usuario
from usuarios.forms import RegistraUsuarioForm


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        if email == '' or password == '':
            messages.error(
                request, 'Os campos email e senha não podem ser vazios')
            return redirect('usuarios:login')

        if Usuario.objects.filter(email=email).exists():
            username = Usuario.objects.get(email=email).username
            user = auth.authenticate(
                request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('app:home')
            else:
                messages.error(
                    request, 'Usuário não cadastrado')
                return redirect('usuarios:login')
        else:
            messages.error(request, 'Usuário não cadastrado')

    return render(request, 'usuarios/login.html')


def criar_conta(request):
    form = RegistraUsuarioForm()
    if request.user.is_anonymous:
        if request.method == 'POST':
            form = RegistraUsuarioForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                email = form.cleaned_data.get('email')
                first_name = form.cleaned_data.get('first_name')
                last_name = form.cleaned_data.get('last_name')
                password1 = form.cleaned_data.get('password1')
                password2 = form.cleaned_data.get('password2')
                form.save()
                novo_usuario = authenticate(
                    username=username, password=password1)
                if novo_usuario is not None:
                    auth_login(request, novo_usuario)
                    messages.success(
                        request, 'Conta criada com sucesso! Acesse o seu email e click no link de confirmação para validar sua conta')
                    return redirect('app:home')
            else:
                return render(request, 'usuarios/criar-conta.html', {'form': form})
        else:
            return render(request, 'usuarios/criar-conta.html', {'form': form})
    else:
        return redirect('app:home')
