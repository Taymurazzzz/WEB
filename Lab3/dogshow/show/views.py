from rest_framework import viewsets
from .serializers import UserSerializer, DogSerializer, DogToShowSerializer, MedicalExaminationSerializer, \
    PlaceSerializer, SponsorSerializer, ShowSerializer, RingSerializer, ExpertSerializer, ExerciseSerializer, CurriculumSerializer
from .models import User, Dog, DogToShow, MedicalExamination, Expert, Exercise, Place, Ring, Sponsor, Curriculum, Show


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class DogViewSet(viewsets.ModelViewSet):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer


class DogToShowViewSet(viewsets.ModelViewSet):
    queryset = DogToShow.objects.all()
    serializer_class = DogToShowSerializer


class MedicalExaminationViewSet(viewsets.ModelViewSet):
    queryset = MedicalExamination.objects.all()
    serializer_class = MedicalExaminationSerializer


class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


class SponsorViewSet(viewsets.ModelViewSet):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer


class ShowViewSet(viewsets.ModelViewSet):
    queryset = Show.objects.all()
    serializer_class = ShowSerializer


class RingViewSet(viewsets.ModelViewSet):
    queryset = Ring.objects.all()
    serializer_class = RingSerializer


class ExpertViewSet(viewsets.ModelViewSet):
    queryset = Expert.objects.all()
    serializer_class = ExpertSerializer


class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer


class CurriculumViewSet(viewsets.ModelViewSet):
    queryset = Curriculum.objects.all()
    serializer_class = CurriculumSerializer
