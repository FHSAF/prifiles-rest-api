from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .views import HelloApiView, HellViewSet, UserProfileViewSet, UserLoginApiView

router = DefaultRouter()
router.register('viewset', HellViewSet, basename='viewset')
router.register('profile', UserProfileViewSet)

urlpatterns = [
    path('APIView', HelloApiView.as_view()),
    path('login/', UserLoginApiView.as_view()),
    path('', include(router.urls))
]
