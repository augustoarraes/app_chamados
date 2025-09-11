from rest_framework import serializers
from .models import User, Chamado

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'celular', 'is_staff', 'is_active')


class ChamadoSerializer(serializers.ModelSerializer):
    aberto_por = UserSerializer(read_only=True)
    tecnico = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False, allow_null=True)

    class Meta:
        model = Chamado
        fields = ('id', 'titulo', 'descricao', 'aberto_por', 'tecnico', 'status', 'prioridade', 'data_criacao', 'data_atualizacao')
        read_only_fields = ('data_criacao', 'data_atualizacao')
        extra_kwargs = {
            'titulo': {'required': True},
            'status': {'required': True},
            'prioridade': {'required': True},
        }
