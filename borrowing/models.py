from django.db import models
from books.models import Book
from members.models import Member
from datetime import datetime, date

class Borrowing(models.Model):
    book=models.ForeignKey(Book,on_delete=models.CASCADE,related_name='borrowing')
    member=models.ForeignKey(Member,on_delete=models.CASCADE,related_name='borrowing')
    borrow_date=models.DateField(auto_now_add=True)
    return_date=models.DateField(null=True,blank=True)
    due_date = models.DateField(null=True, blank=True)

    def is_overdue(self):
        if self.return_date is None and date.today() > self.due_date:
            return True
        return False
    
    def __str__(self):
        return f"{self.member} borrowed {self.book}"
    

