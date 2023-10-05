from django.db import models
from django.db.models import CASCADE

from users.models import NULLABLE


class Course(models.Model):
    title = models.CharField(max_length=150, verbose_name='title')
    description = models.TextField(verbose_name='description')
    image = models.ImageField(verbose_name='image', **NULLABLE)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'course'
        verbose_name_plural = 'courses'


class Lesson(models.Model):
    title = models.CharField(max_length=150, verbose_name='title')
    description = models.TextField(verbose_name='description')
    image = models.ImageField(verbose_name='image', **NULLABLE)
    url_to_video = models.URLField(verbose_name='url_to_video', **NULLABLE)
    url_to_course = models.ForeignKey(Course, on_delete=CASCADE, related_name='lessons', verbose_name='url_to_course', **NULLABLE)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'lesson'
        verbose_name_plural = 'lessons'
