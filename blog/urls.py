from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'), #мы связали view под именем post_list с корневым URL-адресом ('')\
    # Последняя часть name='post_list' — это имя URL, которое будет использовано, чтобы идентифицировать его.
]