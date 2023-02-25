from rest_framework.serializers import Serializer, CharField, IntegerField
from .models import Profile

class ProfileSerializer(Serializer):
    id = IntegerField(read_only=True)
    external_id = IntegerField()
    name = CharField(max_length=128)

    def create(self, validated_data):
        ser_obj = Profile.objects.create(**validated_data)
        return ser_obj

    def update(self, instance, validated_data):
        instance.external_id = validated_data.get('external_id', instance.external_id)
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


