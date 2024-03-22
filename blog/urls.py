from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'), #мы связали view под именем post_list с корневым URL-адресом ('')\
    # Последняя часть name='post_list' — это имя URL, которое будет использовано, чтобы идентифицировать его.
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]

