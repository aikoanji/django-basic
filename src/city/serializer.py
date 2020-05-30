from rest_framework import  serializers
from src.province.serializer import ProvinceSerializer

class CitySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    province = ProvinceSerializer(required=False)