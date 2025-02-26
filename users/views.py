from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import User
from django.contrib.auth import authenticate, login

@csrf_exempt
def register(request):
    if request.method == 'POST':
        data = request.POST
        fullname = data.get('fullname')
        email = data.get('email')
        username = data.get('username')
        password = data.get('password')
        if User.objects.filter(username=username).exists():
            return render(request, 'loginregister.html', {'error': 'Username already exists'})
        if User.objects.filter(email=email).exists():
            return render(request, 'loginregister.html', {'error': 'Email already exists'})
        User.objects.create_user(
            first_name=fullname,
            email=email,
            username=username,
            password=password
            )
    return render(request, 'loginregister.html')

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        data = request.POST
        username = data.get('username')
        password = data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'index.html')
        else:
            return render(request, 'loginregister.html', {'error': 'Invalid credentials'})
        
    return render(request, 'loginregister.html')
