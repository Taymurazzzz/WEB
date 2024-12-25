from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_http_methods
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import AddHotel
from .models import Hotel


def home(request):
    return render(request, 'home.html')

@require_http_methods(["GET"])
def get_hotel_info(request):
    hotel = get_object_or_404(Hotel, id=id)
    return request.user


@require_http_methods(["GET", "POST"])
def add_hotel_info(request):
    form = AddHotel(request.POST)
    if request.method == "POST" and form.is_valid():
        form.save()


def hotel_list(request):
    hotels = Hotel.objects.all()  # Получаем все объекты отелей из базы данных
    return render(request, 'hotel_list.html', {'hotels': hotels})


def create_hotel(request):
    name = request.POST.get('name')
    address = request.POST.get('address')

    hotel = Hotel(name=name, address=address)
    hotel.save()

    return redirect('hotel_list')  # Замените 'hotel_list' на нужный URL


def login_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/')
    else:
        messages.error(request, 'Неверное имя пользователя или пароль.')
    return render(request, 'login.html')


@require_http_methods(["POST", "GET"])
def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 != password2:
            messages.error("Пароли не совпадают")
            return render(request, 'register.html')
        if User.objects.filter(username=username).exists():
            messages.error("Пользователь с таким именем уже существует")
            return render(request, 'register.html')
        if User.objects.filter(email=email).exists():
            messages.error("Пользовотель с такой почтой уже существует")
            return render(request, 'register.html')
        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()
        return redirect('login')
    if request.method == "GET":
        return render(request, 'register.html')


@login_required
def booking_view(request):
    hotels = Hotel.objects.all()
    hotel = request.POST.get('hotel')
    checkin = request.POST.get('checkin')
    checkout = request.POST.get('checkout')
    guests = request.POST.get('guests')
    room_type = request.POST.get('room_type')
    room_quality = request.POST.get('room_quality')
    # TODO: Сравнивать резервировния по диапазонам дат(придумать как реализовать) и отправить список комнат на некст страничку
    return render(request, 'booking.html', {'hotels': hotels})