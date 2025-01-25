from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('book', 'member', 'rating', 'comment', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('book__title', 'member__first_name', 'member__last_name', 'comment')
    date_hierarchy = 'created_at'
