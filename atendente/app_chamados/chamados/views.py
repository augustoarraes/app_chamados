from rest_framework import viewsets, permissions
from .models import User, Chamado
from .serializers import UserSerializer, ChamadoSerializer
from .permissions import QuemPodeResolverChamado
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status


class IsStaffOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]


class ChamadoViewSet(viewsets.ModelViewSet):
    queryset = Chamado.objects.all().select_related('aberto_por', 'tecnico')
    serializer_class = ChamadoSerializer
    permission_classes = [permissions.IsAuthenticated, QuemPodeResolverChamado]

    def perform_create(self, serializer):
        serializer.save(aberto_por=self.request.user)
