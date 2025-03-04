from datetime import datetime
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


def get_example(request):

    response = {'request': {'time': datetime.now().isoformat(),
                            'method': request.method,
                            'path': request.path,
                            'params': request.GET,
                            'headers': dict(request.headers)}}
    # response = 'hola'

    return JsonResponse(response, safe=False, json_dumps_params={'indent': 2})


@csrf_exempt
def post_example(request):
    response = {'request': {'time': datetime.now().isoformat(),
                'method': request.method,
                'path': request.path,
                'params': request.GET,
                'headers': dict(request.headers),
                'body': request.body.decode()}}
    return JsonResponse(response, safe=False, json_dumps_params={'indent': 2})


def gallery(request):
    return render(request, 'testapp/gallery.html')


def gallery_photo(request, photo):
    context = {'photo': photo}
    return render(request, 'testapp/gallery_photo.html', context)


def calculadora(request, numero1, operacion, numero2):
    if operacion == "sumar":
        respuesta = int(numero1) + int(numero2)
    if operacion == "restar":
        respuesta = int(numero1) - int(numero2)
    if operacion == "multiplicar":
        respuesta = int(numero1) * int(numero2)
    if operacion == "dividir":
        respuesta = int(numero1) / int(numero2)
    return JsonResponse(respuesta, safe=False, json_dumps_params={'indent': 2})