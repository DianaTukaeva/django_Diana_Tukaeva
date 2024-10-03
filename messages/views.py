from django.http import HttpResponse

# Create your views here.
def main(request):
    return HttpResponse('Вау, ты на странице сообщений!')

def dialog(request):
    return HttpResponse('А теперь ты на странице диалога!!')

def emoji(request):
    return HttpResponse('Вау, ты открыл эмоджи')