from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    passport = models.CharField(max_length=10, blank=True)
    patronymic = models.CharField(max_length=50, blank=True)
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="show_users",
        blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="show_users_permissions",
        blank=True
    )

class Dog(models.Model):
    name = models.CharField(max_length=50)
    club = models.CharField(max_length=50)
    breed = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    classRanking = models.CharField(max_length=50)
    document = models.CharField(max_length=20)
    mother_name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

class MedicalExamination(models.Model):
    doctor = models.CharField(max_length=150)
    date = models.DateTimeField(null=True)
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
    result = models.BooleanField(default=False)

class Place(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    capacity = models.IntegerField(default=0)

class Sponsor(models.Model):
    name = models.CharField(max_length=100)
    info = models.CharField(max_length=200)
    advertisement = models.CharField(max_length=100)

class Show(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField(null=True)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    sponsor = models.ManyToManyField(Sponsor)

class Ring(models.Model):
    number = models.IntegerField(default=0)
    show = models.ForeignKey(Show, on_delete=models.CASCADE)

class Expert(models.Model):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    club = models.CharField(max_length=50)
    ring = models.ForeignKey(Ring, on_delete=models.DO_NOTHING)

class Exercise(models.Model):
    first = models.IntegerField(default=0)
    second = models.IntegerField(default=0)
    third = models.IntegerField(default=0)
    expert = models.OneToOneField(Expert, on_delete=models.CASCADE)

    @property
    def total(self):
        return self.first + self.second + self.third

class DogToShow(models.Model):
    dog = models.OneToOneField(Dog, on_delete=models.CASCADE)
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    payment = models.BooleanField(default=False)
    ring = models.ForeignKey(Ring, on_delete=models.CASCADE, blank=True, null=True)
    result = models.OneToOneField(Exercise, on_delete=models.CASCADE, blank=True, null=True)

    @property
    def result_sum(self):
        return self.result.total if self.result else 0

class Curriculum(models.Model):
    start_time = models.TimeField(null=True)
    end_time = models.TimeField(null=True)
    breed = models.CharField(max_length=100)
    ring = models.ManyToManyField(Ring)
    show = models.ForeignKey(Show, on_delete=models.CASCADE)