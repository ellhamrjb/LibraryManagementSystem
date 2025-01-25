from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet, BookViewSet, GenreViewSet, PublisherViewSet,book_list,book_detail
from . import views

router = DefaultRouter()
router.register('authors', AuthorViewSet)
router.register('books', BookViewSet)
router.register('genres', GenreViewSet)
router.register('publishers', PublisherViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', book_list, name='books-list'),
    path('<int:pk>/', book_detail, name='book-detail'),
    path('list/', views.book_list, name='books-list'),
]
