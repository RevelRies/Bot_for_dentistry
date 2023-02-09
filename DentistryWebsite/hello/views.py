from django.http import HttpResponse, HttpRequest, HttpResponseBadRequest, JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render

def index(request: HttpRequest):
    data = {'name': 'nikita'}

    return render(request, 'index.html', context=data)