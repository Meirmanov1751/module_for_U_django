from django.contrib import admin
from .models import Reference, ReferenceType

# Register your models here.
admin.site.register(Reference)
admin.site.register(ReferenceType)

