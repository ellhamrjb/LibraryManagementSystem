from django.db import models

class Genre(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField(blank=True)

    def __str__(self):
        return self.name
    
class Publisher(models.Model):
    name=models.CharField(max_length=255)
    website=models.URLField(blank=True)
    email=models.EmailField(blank=True)

    def __str__(self):
        return self.name
    
class Author(models.Model):
    name=models.CharField(max_length=255)
    bio=models.TextField(blank=True)
    date_of_birth=models.DateField(null=True,blank=True)
    nationality=models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.name
    
class Book(models.Model):
    title=models.CharField(max_length=255)
    author=models.ForeignKey(Author,on_delete=models.CASCADE,related_name='books')
    genre=models.ForeignKey(Genre, on_delete=models.CASCADE,related_name='books')
    publisher=models.ForeignKey(Publisher,on_delete=models.CASCADE,related_name='books')
    isbn=models.CharField(max_length=13,unique=True)
    published_date=models.DateField()
    copies_available=models.PositiveIntegerField(default=0)
    cover_image=models.ImageField(upload_to='book_covers/',blank=True,null=True)

    def __str__(self):
        return self.title
