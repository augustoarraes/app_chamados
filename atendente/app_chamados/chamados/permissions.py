from rest_framework import permissions


class QuemPodeResolverChamado(permissions.BasePermission):
    """
    Permissão só o técnico pode mudar para “Resolvido”. 
    Ou seja, esse status o atendente não tem permissão de atualizar
    """

    def has_object_permission(self, request, view, obj):
        # Só verifica se for uma atualização
        if request.method in ["PUT"]:
            new_status = request.data.get("status")
            if new_status == "Resolvido":
                return request.user.groups.filter(name="Tecnico").exists()
        return True
