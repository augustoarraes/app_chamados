from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Chamado
from django.utils.translation import gettext_lazy as _


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'celular')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)


@admin.register(Chamado)
class ChamadoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'status', 'prioridade', 'aberto_por', 'tecnico', 'data_criacao', 'data_atualizacao')
    list_filter = ('status', ) # 'prioridade', 'data_criacao', 'tecnico'
    search_fields = ('titulo', 'descricao', 'aberto_por__username', 'tecnico__username')
    readonly_fields = ('aberto_por', 'data_criacao', 'data_atualizacao',)
    #autocomplete_fields = ('tecnico')

    def get_changeform_initial_data(self, request):
        return {"aberto_por": request.user.id}

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.aberto_por = request.user
        super().save_model(request, obj, form, change)