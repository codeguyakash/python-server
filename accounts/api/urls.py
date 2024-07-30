# from django.urls import include, path
# from rest_framework import routers
# from . import views
# from .views import LoginAPIView,LogoutAPIView


# router = routers.DefaultRouter()
# router.register(r'register', views.UserViewSet, basename='register')

# urlpatterns = [
#     path('', include(router.urls)),
#     path('login/', LoginAPIView.as_view(), name='login'),
#     path('logout/', LogoutAPIView.as_view(), name='logout'),
   
# ]

from django.urls import include, path
from rest_framework import routers
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)






router = routers.DefaultRouter()
router.register(r'register', views.UserViewSet, basename='register')

urlpatterns = [
    path('', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/logout/', views.LogoutAPIView.as_view(), name='logout'),


    

    
]
