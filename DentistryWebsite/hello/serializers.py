from rest_framework.serializers import ModelSerializer
from .models import Profile

class ProfileAPISerializer(ModelSerializer):

    class Meta:
        model = Profile
        fields = ('external_id', 'name')