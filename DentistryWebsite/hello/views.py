from .models import Profile
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from .serializers import ProfileAPISerializer


class ProfileAPI(APIView):
    def get(self, request: Request):
        res = Profile.objects.all().values()
        return Response(res)

# class ProfileAPI(ListAPIView):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileAPISerializer
