from django.http import HttpResponse, HttpRequest, HttpResponseBadRequest, JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render

def base(request: HttpRequest):
    return render(request=request, template_name='base.html')


def info(request: HttpRequest):
    return render(request=request, template_name='info.html')


def contact(request: HttpRequest):
    return render(request=request, template_name='contact.html')


def user(request: HttpRequest):
    name = request.POST.get('name', 'Не введено')
    age = request.POST.get('age', 0)
    l1, l2, l3 = request.POST.getlist('languages')
    return HttpResponse(f'<h2>Имя: {name}</h2>'
                        f'<h2>Возраст: {age}</h2>'
                        f'<h2>Языки:</h2>'
                        f'<p>{l1}</p>'
                        f'<p>{l2}</p>'
                        f'<p>{l3}</p>')


def index(request: HttpRequest):
    return render(request=request, template_name='userform.html')