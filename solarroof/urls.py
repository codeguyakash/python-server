
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

# admin.site.site_header = settings.ADMIN_SITE_HEADER
router = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'api/accounts/', include('accounts.api.urls')),
    path(r'api/state/', include('statecity.api.urls')),
    path(r'api/contact/', include('contact.api.urls')),
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path(r'api/warrentycard/', include('warrentycard.api.urls')),
    path(r'api/solar/', include('Solar.api.urls')),


    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

