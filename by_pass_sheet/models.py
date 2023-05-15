from django.db import models

from student.models import Student
from user.models import User


# Create your models here.
class BypassSheet(models.Model):
    title = models.CharField(max_length=100)
    text1 = models.TextField()
    text2 = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Bypass Sheet - {self.title}"

class BypassSheetField(models.Model):
    name = models.CharField(max_length=100)
    bypass_sheet = models.ForeignKey(BypassSheet, on_delete=models.CASCADE, related_name="bypass_sheet_field")

    def __str__(self):
        return self.name
