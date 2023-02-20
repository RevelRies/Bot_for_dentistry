from django.http import HttpResponse, HttpRequest, HttpResponseBadRequest, JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render
from .models import Person, Doctor


