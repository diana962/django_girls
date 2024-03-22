from django.conf import settings # not clear?
from django.db import models
from django.utils import timezone # to take data of timezone


class Post(models.Model): #models.Model означает, что объект Post является моделью Django, \
    # так Django поймет, что он должен сохранить его в базу данных.
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    # models.CharField — так мы определяем текстовое поле с ограничением на количество символов.
    # models.TextField — так определяется поле для неограниченно длинного текста.
    # models.DateTimeField — дата и время.
    # models.ForeignKey — ссылка на другую модель.

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title