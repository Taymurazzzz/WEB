from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import User


class Hotel(models.Model):
    name = models.CharField(max_length=80)
    owner_name = models.CharField(max_length=80, default="Не установлен")
    address = models.CharField(max_length=100)
    description = models.CharField(max_length=200, default="Пока здесь пусто")

    def __str__(self):
        return self.name


class Room(models.Model):
    number = models.IntegerField()
    price_per_night = models.IntegerField()
    room_type = models.CharField(
        max_length=50,
        choices=[('single', 'Single'), ('double', 'Double'), ('twin', 'Twin'), ('triple', 'Triple'),
                 ('quadriple', 'Quadriple')]
    )
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    capacity = models.IntegerField()
    quality = models.CharField(
        max_length=50,
        choices=[('standard', 'Standard'), ('superior', 'Superior'), ('lux', 'Lux')]
    )


class Reservation(models.Model):
    visitor = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)


class Review(models.Model):
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    user_nick = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    created_at = models.DateField(auto_now_add=True)
    rating = models.IntegerField(validators=[
            MinValueValidator(1),
            MaxValueValidator(10)
        ])
