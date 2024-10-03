from django.urls import path
from news.views import main, detail, redactor

urlpatterns = [
    path('', main),
    path('detail/', detail),
    path('redactor/', redactor),
]