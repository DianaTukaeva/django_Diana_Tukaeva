from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('registration.urls')),
    path('messages/', include('messages.urls')),
    path('news/', include('news.urls')),
]
