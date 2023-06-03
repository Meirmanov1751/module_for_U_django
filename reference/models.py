from django.db import models

from user.models import User

class ReferenceType(models.Model):
    title = models.CharField(max_length=100)
    text1 = models.TextField()
    text2 = models.TextField()

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Тип справки'
        verbose_name_plural = 'Типы справки'


class Reference(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Ожидание'),
        ('approved', 'Подтверждено'),
        ('rejected', 'Отклонено'),
    ]

    student = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    info = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='pending', null=True, blank=True)
    reference_type = models.ForeignKey(
        ReferenceType,
        on_delete=models.CASCADE,
         null=True, blank=True
    )

    def __str__(self):
        return f" {self.student}"

    class Meta:
        verbose_name = 'Справка'
        verbose_name_plural = 'Справки'

