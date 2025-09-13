from drf_spectacular.utils import extend_schema
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


@extend_schema(
    tags=["Autenticação"],
    summary="Obter token JWT",
    description="Endpoint para autenticação. Envie username e password para receber os tokens de acesso e refresh.",
    responses={200: dict},
)
class CustomTokenObtainPairView(TokenObtainPairView):
    pass


@extend_schema(
    tags=["Autenticação"],
    summary="Atualizar token JWT",
    description="Endpoint para renovar o token de acesso a partir do refresh token.",
    responses={200: dict},
)
class CustomTokenRefreshView(TokenRefreshView):
    pass
