from django.http import HttpResponse

def main(request):
    return HttpResponse('Ты на странице новостей)')

def detail(request):
    return HttpResponse('Теперь ты открыл конкретную новость :)')

def redactor(request):
    return HttpResponse('Боже, ты тут сам можешь написать новость :D')
