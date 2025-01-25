from django.db import models
from books.models import Book
from members.models import Member


class Review(models.Model):
    book=models.ForeignKey(Book,on_delete=models.CASCADE,related_name='reviews')
    member=models.ForeignKey(Member,on_delete=models.CASCADE,related_name='reviews')
    rating=models.PositiveSmallIntegerField()
    comment=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.member} rated {self.book} ({self.rating/5})"