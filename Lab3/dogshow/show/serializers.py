from rest_framework import serializers
from .models import User, Dog, DogToShow, Ring, Curriculum, Sponsor, Show, MedicalExamination, Place, Expert, Exercise


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        ref_name = 'ShowAppUserSerializer'

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = super().create(validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user



class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = '__all__'


class MedicalExaminationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalExamination
        fields = '__all__'


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'


class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = '__all__'


class ShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Show
        fields = '__all__'


class RingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ring
        fields = '__all__'


class ExpertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expert
        fields = '__all__'


class ExerciseSerializer(serializers.ModelSerializer):
    totalScore = serializers.IntegerField(read_only=True, source='total')

    class Meta:
        model = Exercise
        fields = '__all__'


class DogToShowSerializer(serializers.ModelSerializer):
    resultSum = serializers.IntegerField(read_only=True, source='result_sum')

    class Meta:
        model = DogToShow
        fields = '__all__'


class CurriculumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curriculum
        fields = '__all__'
