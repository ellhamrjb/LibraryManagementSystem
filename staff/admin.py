from django.contrib import admin
from .models import Staff

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'position', 'hire_date')
    list_filter = ('position', 'hire_date')
    search_fields = ('first_name', 'last_name', 'email', 'position')
    date_hierarchy = 'hire_date'
