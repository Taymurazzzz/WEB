from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_http_methods
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import AddHotel
from .models import Hotel, Reservation, Room, Review
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from dateutil.parser import parse



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
    if request.method == "POST":
        reservations = list(Reservation.objects.all().order_by('room').filter(start_date__gte=date.today()))
        hotel = request.POST.get('hotel')
        checkin = datetime.strptime(request.POST.get('checkin'), "%Y-%m-%d").date()
        checkout = datetime.strptime(request.POST.get('checkout'), "%Y-%m-%d").date()
        print(checkout)
        if checkin >= checkout or checkin < date.today():
            return render(request, 'booking.html', {'error': 'Invalid date range.'})
        rooms = set(Room.objects.filter(hotel=hotels.get(name=hotel).pk))
        suitable_rooms = set()
        reserved_room = set()
        for reservation in reservations:
            reserved_room.add(reservation.room)
            start = reservation.start_date
            end = reservation.end_date
            if checkin >= end or checkout <= start:
                suitable_rooms.add(reservation.room)
        free_rooms = rooms - reserved_room
        rooms_list = free_rooms.union(suitable_rooms)
        return render(request, "rooms_list.html", {"rooms": rooms_list, "checkin": checkin, "checkout": checkout})

    return render(request, 'booking.html', {'hotels': hotels})


def reserve_view(request, room_id):
    if request.method == "POST":
        checkin = parse(request.POST.get('checkin')).date()
        checkout = parse(request.POST.get('checkout')).date()
        room = Room.objects.get(id=room_id)
        Reservation.objects.create(
            visitor=request.user,
            room=room,
            start_date=checkin,
            end_date=checkout
        ).save()

    return redirect("/")


# TODO: Сделать страничку для визуализавции резерваций активные и прошлые(история броней) с возможностью удаления активных
@login_required
def reservations_list_view(request):
    active_reservation = Reservation.objects.filter(start_date__gte=date.today())
    past_reservations = Reservation.objects.filter(start_date__lt=date.today())
    return render(request, "reservations.html",
                  {"active_reservations": active_reservation, "past_reservations": past_reservations})


@login_required
def cancel_reservation(request, reservation_id):
    if request.method == "POST":
        reservation = Reservation.objects.get(id=reservation_id)
        if reservation:
            reservation.delete()
        return redirect("reservations")

@login_required
def review_view(request):
    user = request.user
    reservations = Reservation.objects.filter(visitor=user)
    rooms = set()
    for reservation in reservations:
        rooms.add(reservation.room)
    if request.method == "POST":
        text = request.POST.get("review")
        rating = request.POST.get("rating")
        room = list(rooms)[int(request.POST.get("room")) - 1]
        review = Review.objects.create(room_id=room, user_nick=user, text=text, rating=int(rating))
        review.save()
        return redirect("/")
    return render(request, 'review.html', {"ratings": range(1, 11), "rooms": rooms})


def review_list(request):
    reviews = Review.objects.all()
    reviews_data = []
    for review in reviews:
        reservation = Reservation.objects.filter(visitor=review.user_nick, room=review.room_id).latest("end_date")
        date_period = f"С {reservation.start_date} по {reservation.end_date}"
        reviews_data.append({
            "user": review.user_nick.username,
            "created_at": review.created_at,
            "room": f"{review.room_id.number} в отеле {review.room_id.hotel.name}",
            "stay_period": date_period,
            "rating": review.rating,
            "text": review.text
        })
    return render(request, "show_review.html", {"reviews": reviews_data})


def guests_list_view(request):
    month = date.today() - relativedelta(months=1)
    hotels = Hotel.objects.all()
    hotels_data = []
    for hotel in hotels:
        visitors = Reservation.objects.select_related("visitor").filter(start_date__gt=month, room__hotel=hotel)
        hotels_data.append({
            "hotel": hotel.name,
            "guests": visitors
        })
    return render(request, "guests.html", {'hotels_data': hotels_data})


'''
        for reservation in reservations:
            reserved_room_ids.add(reservation.room_id)
            start = reservation.start_date
            end = reservation.end_date
            try:
                next_start = reservations[reservations.index(reservation) + 1].start_date
                next_end = reservations[reservations.index(reservation) + 1].end_date
                next_room_id = reservations[reservations.index(reservation) + 1].room
            except IndexError:
                next_start = 0
                next_end = 0
                next_room_id = 0
            print(next_start)
            if reservation.room.hotel == hotel:
                if start <= checkin < end or start < checkout <= end:
                    continue
                elif checkout <= start or checkin >= end:
                    if next_start <= checkin < next_end or next_start < checkout and reservation.room == next_room_id:
                        continue
                    elif checkout <= next_start and reservation.room == next_room_id:
                        suitable_rooms.add(reservation.room_id)
            else:
                continue
            print(suitable_rooms)
'''
