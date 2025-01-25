from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReviewViewSet, review_list

router = DefaultRouter()
router.register('reviews', ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', review_list, name='reviews-list'),
]
