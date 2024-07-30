from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .import views

router = DefaultRouter()
router.register(r'state', views.StateSubsidyViewSet)
router.register(r'city', views.CityViewset,basename='city')

urlpatterns = [
    path('', include(router.urls)),
]
