from django.http import HttpResponse

def main(request):
    return HttpResponse('Зарегистрируйся!')

def data(request):
    return HttpResponse('Зайди на сайт!')

def incorrect(request):
    return HttpResponse('Упс, вылезла ошибка(((')