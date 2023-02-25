from rest_framework import serializers
from .models import Profile
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from .serializers import ProfileSerializer


class ProfileAPI(APIView):
    def get(self, request: Request):
        res = Profile.objects.all()
        return Response(ProfileSerializer(res, many=True).data)


    def post(self, request: Request):
        data = request.data

        #проверка входных данных
        ser_obj = ProfileSerializer(data=data)
        ser_obj.is_valid(raise_exception=True)

        #сохранение в БД
        ser_obj.save()

        return Response(f'Пользователь создан: {ser_obj.data}')


    def put(self, request: Request, *args, **kwargs):
        data = request.data
        pk = kwargs['pk']
        instance = Profile.objects.get(id=pk)

        # проверка входных данных
        ser_obj = ProfileSerializer(instance=instance, data=data)
        ser_obj.is_valid(raise_exception=True)
        ser_obj.save()

        return Response(ser_obj.data)


    def delete(self, request: Request, **kwargs):
        pk = kwargs['pk']
        Profile.objects.get(id=pk).delete()

        return Response('Пользователь удален')

