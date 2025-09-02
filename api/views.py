# views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        username = request.POST.get('usuario')
        password = request.POST.get('password')

        # Intentar autenticar al usuario
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Si la autenticación es exitosa, inicia sesión y redirige al home
            login(request, user)
            return redirect('home')  # Redirige a la vista 'home' (no al archivo HTML)
        else:
            # Si las credenciales son incorrectas, muestra un mensaje de error
            messages.error(request, 'Usuario o contraseña incorrectos')

    # Si no es un POST, simplemente muestra el formulario
    return render(request, 'login.html')

def home_view(request):
    return render(request, 'home.html')  # Renderiza el archivo home.html

def logout_view(request):
    return redirect('login')