"""
URL configuration for hotelservice project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import get_hotel_info, create_hotel, hotel_list, login_view, register, home, booking_view, review_view, review_list, guests_list_view, reserve_view, reservations_list_view, cancel_reservation

urlpatterns = [
    path('', home),
    path('hotels/', hotel_list, name='hotel_list'),
    path('create_hotel/', create_hotel, name='create_hotel'),
    path("test/", get_hotel_info),
    path("admin/", admin.site.urls),
    path("login/", login_view, name='login'),
    path("register/", register),
    path("booking/", booking_view, name='booking'),
    path("review/", review_view, name="review"),
    path("reviews/", review_list, name="reviews"),
    path("guests/", guests_list_view, name="guests"),
    path("reserve/<int:room_id>/", reserve_view, name="reserve"),
    path("reservations/", reservations_list_view, name="reservations"),
    path("cancel_reservation/<int:reservation_id>", cancel_reservation, name="cancel_reservation")
]
