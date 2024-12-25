from django.contrib import admin
from .models import Hotel, Reservation, Room, Review


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner_name', 'address', 'description')
    search_fields = ('name', 'owner_name')


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'price_per_night', 'room_type', 'hotel', 'quality')


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('id', 'visitor', 'room_id', 'start_date', 'end_date')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'room_id', 'user_nick', 'text', 'rating')
