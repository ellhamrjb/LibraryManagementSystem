from rest_framework import serializers
from .models import Review
from books.serializers import BookSerializer
from members.serializers import MemberSerializer

class ReviewSerializer(serializers.ModelSerializer):
    book = BookSerializer()
    member = MemberSerializer()

    class Meta:
        model = Review
        fields = ['id', 'book', 'member', 'rating', 'comment', 'created_at']
