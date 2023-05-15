from django.db import models

# Create your models here.
class Student(models.Model):
    group = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'