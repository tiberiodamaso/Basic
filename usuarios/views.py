from django.contrib import auth, messages
from django.contrib.auth.models import User
from usuarios.models import Usuario
from django.shortcuts import render, redirect


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
