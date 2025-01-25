from rest_framework import serializers
from .models import Book,Author,Genre,Publisher

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model=Genre
        fields=['id','name','description']

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['id', 'name', 'website', 'email']

class AuthorSerializer(serializers.ModelSerializer):
    books = serializers.StringRelatedField(many=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'bio', 'date_of_birth', 'nationality', 'books']

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    genre = GenreSerializer(many=True)
    publisher = PublisherSerializer()

    class Meta:
        model = Book
        fields = [
            'id', 'title', 'author', 'genre', 'publisher', 'isbn',
            'published_date', 'copies_available', 'cover_image'
        ]