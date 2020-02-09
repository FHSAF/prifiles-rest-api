from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .views import HelloApiView, HellViewSet

router = DefaultRouter()
router.register('viewset', HellViewSet, basename='viewset')

urlpatterns = [
    path('APIView', HelloApiView.as_view()),
    path('', include(router.urls))
]
