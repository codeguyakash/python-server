from django.urls import path, include
from rest_framework.routers import DefaultRouter
from.import views

router = DefaultRouter()
router.register(r'inquiries', views.SolarInquiryViewSet,basename='inquires')
router.register(r'status', views.SolarStatusViewSet,basename='inqstatus')
router.register(r'maintance', views.SolarMaintanceViewSet,basename='maintance')
router.register(r'maintancestatus', views.MaintanceStatusViewSet,basename='maintancestatus')



urlpatterns = [
    path('', include(router.urls)),
    path('api/contact/', include(router.urls)),

]
