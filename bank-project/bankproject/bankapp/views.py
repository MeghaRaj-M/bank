from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect

from .forms import AccountForm
from .models import District
from .models import Branch


# Create your views here.
def home_page(request):
    return render(request, 'home.html')


def kozhikode(request):
    return render(request, 'kozhikode.html')


def kannur(request):
    return render(request, 'kannur.html')


def alappuzha(request):
    return render(request, 'alappuzha.html')


def trivandrum(request):
    return render(request, 'trivandrum.html')


def trissur(request):
    return render(request, 'trissur.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpass = request.POST['cpass']
        if password == cpass:
            if User.objects.filter(username=username).exists():
                messages.info(request, "User already exist")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request, "Password does not match")
            return redirect('register')
    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return render(request, 'user_page.html')
        else:
            messages.info(request, "Invalid credentials")
            return redirect('login')
    return render(request, 'login.html')


def add_account(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = AccountForm()

    return render(request, 'add_account.html', {'form': form, 'districts': District.objects.all()})


def get_branches(request):
    district_slug = request.GET.get('district')
    if district_slug:
        branches = Branch.objects.filter(district__slug=district_slug)
        data = [{'slug': branch.slug, 'branch': branch.branch} for branch in branches]
    else:
        data = []
    return JsonResponse(data, safe=False)


def logout(request):
    auth.logout(request)
    return redirect('/')
