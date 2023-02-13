from django.http import HttpResponse, HttpRequest, HttpResponseBadRequest, JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render

def base(request: HttpRequest):
    return render(request=request, template_name='base.html')


def info(request: HttpRequest):
    return render(request=request, template_name='info.html')


def contact(request: HttpRequest):
    return render(request=request, template_name='contact.html')