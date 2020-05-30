from rest_framework import serializers
from src.province.models import Province

class ProvinceSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(allow_null=False, allow_blank=False)
    created_at = serializers.DateTimeField(required=False, write_only=True)
    modified_at = serializers.DateTimeField(required=False, write_only=True)

    def create(self, validated_data):
        return Province.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance