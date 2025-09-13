from rest_framework import routers
from .views import ChamadoViewSet, UserViewSet
from django.urls import path, include
from .schema import CustomTokenObtainPairView, CustomTokenRefreshView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = routers.DefaultRouter()
router.register(r'chamados', ChamadoViewSet)
router.register(r'users', UserViewSet, basename='user')


urlpatterns = [
    path('', include(router.urls)),

    # JWT endpoints:
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
]
