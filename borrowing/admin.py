from django.contrib import admin
from .models import Borrowing

@admin.register(Borrowing)
class BorrowingAdmin(admin.ModelAdmin):
    list_display = ('book', 'member', 'borrow_date', 'due_date', 'return_date', 'is_overdue')  # No changes needed here
    list_filter = ('borrow_date', 'return_date')
    search_fields = ('book__title', 'member__first_name', 'member__last_name')
    date_hierarchy = 'borrow_date'

    def is_overdue(self, obj):
        return obj.is_overdue()
    is_overdue.boolean = True
    is_overdue.short_description = 'Overdue?'
