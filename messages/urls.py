from django.urls import path
from messages.views import main, dialog, emoji

urlpatterns = [
    path('', main),
    path('dialog/', dialog),
    path('emoji/', emoji),
]