from django.contrib import admin
from .models import Member, Role

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'membership_date', 'role')
    list_filter = ('membership_date', 'role')
    search_fields = ('first_name', 'last_name', 'email')
    date_hierarchy = 'membership_date'

