from django.urls import path
from registration.views import main, data, incorrect

urlpatterns = [
    path('', main),
    path('data/', data),
    path('incorrect/', incorrect)
]