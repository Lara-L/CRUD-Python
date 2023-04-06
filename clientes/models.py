from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    data_nascimento = models.DateField()
    email = models.EmailField()

class Pagamento(models.Model):
    forma_de_pagamento = models.CharField(max_length=255)
    valor_pago = models.FloatField()

class Viagem(models.Model):
    nome = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    estado = models.CharField(max_length=2)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    pagamento = models.ForeignKey(Pagamento, on_delete=models.CASCADE)