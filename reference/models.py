from django.db import models

from student.models import Student
from user.models import User

class ReferenceType(models.Model):
    title = models.CharField(max_length=100)
    text1 = models.TextField()
    text2 = models.TextField()

    def __str__(self):
        return f"{self.title}"


class Reference(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Ожидание'),
        ('approved', 'Подтверждено'),
        ('rejected', 'Отклонено'),
    ]

    student = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    info = models.TextField()
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='pending', null=True, blank=True)
    reference_type = models.ForeignKey(
        ReferenceType,
        on_delete=models.CASCADE,
         null=True, blank=True
    )

    def __str__(self):
        return f" {self.student}"


