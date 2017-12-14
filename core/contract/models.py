# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

#Mixin
from mixin.timefield import TimeFieldMixin
# Create your models here.

class Contract(TimeFieldMixin, models.Model):
    
    title = models.CharField('Titulo', max_length=255, blank=True, null=True)
    description = models.TextField('Descrição')
    user = models.ForeignKey(User, related_name='user', on_delete=False)
    STATUS_CHOICES = (
        ('Pedente', 'Pendente'),
        ('Em_andamento', 'Em_andamento'),
        ('Finzalizado', 'Finalizado')
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Pendente")
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = 'Contrato'
        verbose_name_plural = 'Contratos'

    
class Payment(models.Model):

    description = models.TextField('Descrição')
    contract = models.ForeignKey(Contract, related_name='contract', on_delete=True)
    date_payment = models.DateTimeField('Data de pagamento', auto_now_add=True)
    value = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.description 
    
    class Meta:
        verbose_name = 'Pagamento'
        verbose_name_plural = 'Pagamentos'

