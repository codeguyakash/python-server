from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .import views

router = DefaultRouter()
router.register(r'warranty-cards', views.WarrantyCardUploadViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
