from django.http import HttpResponse


def index(request):
    return HttpResponse(
        'Hello world from Django!\nPrueba iso-8859-1: áéíóúñ',
        content_type='text/plain', charset='iso-8859-1'
    )

