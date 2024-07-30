# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .import views

# router = DefaultRouter()
# router.register(r'solar-calculators', views.SolarCalculatorViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
# ]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'solar-calculators', views.SolarCalculatorViewSet)

urlpatterns = [
        path('', include(router.urls)),

]
