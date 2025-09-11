from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    celular = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.get_full_name() or self.username} ({self.email})"



class Chamado(models.Model):
    STATUS_CHOICES = (
        ('open', 'Aberto'),
        ('in_progress', 'Em Antedimento'),
        ('resolved', 'Resolvido'),
        ('closed', 'Cancelado'),
    )

    PRIORITY_CHOICES = (
        ('low', 'Baixa'),
        ('medium', 'Média'),
        ('high', 'Alta'),
        ('critical', 'Crítica'),
    )

    titulo = models.CharField(max_length=255)
    descricao = models.TextField(blank=True)
    prioridade = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='medium')
    setor = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')
    
    aberto_por = models.ForeignKey('User', related_name='created_tickets', on_delete=models.SET_NULL, null=True, blank=True)
    tecnico = models.ForeignKey('User', related_name='assigned_tickets', on_delete=models.SET_NULL, null=True, blank=True)
    
    data_criacao = models.DateTimeField(default=timezone.now)
    data_atualizacao = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        #return f"[{self.get_priority_display()}] {self.titulo}"
        return f"{self.titulo}"