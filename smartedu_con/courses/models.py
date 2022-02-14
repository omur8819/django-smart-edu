from email.policy import default
from xxlimited import Str
from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name="Kurs Adı", help_text="Kurs adını yazınız")
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="courses/%Y/%m/%d/", default="courses/default_course_image.jpg")
    date = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name