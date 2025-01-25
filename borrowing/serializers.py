from rest_framework import serializers
from .models import Borrowing
from books.serializers import BookSerializer
from members.serializers import MemberSerializer

class BorrowingSerializer(serializers.ModelSerializer):
    book = BookSerializer()
    member = MemberSerializer()
    overdue = serializers.SerializerMethodField()

    class Meta:
        model = Borrowing
        fields = ['id', 'book', 'member', 'borrow_date', 'due_date', 'return_date', 'overdue']

    def get_overdue(self, obj):
        return obj.is_overdue()
