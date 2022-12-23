from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from rental.models import LGA, City, Country, State


class CountrySerializer(ModelSerializer):
    class Meta:
        model = Country
        fields = ("id", "name", "country_code")


class StateSerializer(ModelSerializer):
    country = serializers.PrimaryKeyRelatedField(queryset=Country.objects.all())
    class Meta:
        model = State
        fields = ("id", "name", "country")


class LGASerializer(ModelSerializer):
    class Meta:
        model = LGA
        fields = ("id", "name", "state")


class CitySerializer(ModelSerializer):
    class Meta:
        model = City
        fields = ("id", "name", "state")
