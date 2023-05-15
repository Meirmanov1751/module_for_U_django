from django.contrib import admin
from .models import BypassSheet, BypassSheetField

class BypassSheetInline(admin.TabularInline):  # Или используйте admin.StackedInline для вертикального отображения
    model = BypassSheetField
    extra = 4

@admin.register(BypassSheet)
class BypassSheetFieldAdmin(admin.ModelAdmin):
    inlines = [BypassSheetInline]