from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NikkiViewSet

router = DefaultRouter()
router.register('nikki', NikkiViewSet)

urlpatterns = [
    path('', include(router.urls)),
]