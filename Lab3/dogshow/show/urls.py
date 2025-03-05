from django.urls import include, path
from rest_framework import routers
from .views import UserViewSet, DogViewSet, MedicalExaminationViewSet, PlaceViewSet, SponsorViewSet, ShowViewSet, RingViewSet, ExpertViewSet, ExerciseViewSet, DogToShowViewSet, CurriculumViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'dogs', DogViewSet)
router.register(r'medical-exam', MedicalExaminationViewSet)
router.register(r'places', PlaceViewSet)
router.register(r'sponsors', SponsorViewSet)
router.register(r'shows', ShowViewSet)
router.register(r'rings', RingViewSet)
router.register(r'experts', ExpertViewSet)
router.register(r'exercises', ExerciseViewSet)
router.register(r'participating-dogs', DogToShowViewSet)
router.register(r'curriculums', CurriculumViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
