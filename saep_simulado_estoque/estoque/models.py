from django.db import models

class Movimentacoes(models.Model):
    unique_id = models.AutoField(primary_key=True)
    equipamento = models.ForeignKey('Equipamentos', on_delete=models.CASCADE)
    quantidade = models.IntegerField(null=False, blank=False)
    data = models.DateField(null=False, blank=False, auto_now_add=True)
    fornecedor = models.CharField(max_length=100, null=False, blank=False)
    lote = models.CharField(max_length=50, null=False, blank=False)
    tipo_operacao = models.CharField(
        max_length=20,
        choices=[
            ('entrada', 'Entrada'),
            ('saida', 'Saída')
        ],
        null=False, 
        blank=False
    )

    def __str__(self):
        return f'{self.tipo_operacao} - {self.equipamento} ({self.quantidade})'

class Equipamentos(models.Model):
    unique_id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50, null=False, blank=False)
    tipo = models.ForeignKey('Tipos', on_delete=models.CASCADE)
    tensao = models.DecimalField(max_digits=10, null=False, blank=False, decimal_places=2)
    peso_u = models.DecimalField(max_digits=10, null=False, blank=False, decimal_places=2)
    altura_u = models.DecimalField(max_digits=10, null=False, blank=False, decimal_places=2)
    largura_u = models.DecimalField(max_digits=10, null=False, blank=False, decimal_places=2)
    profundidade_u = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    resolucao = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    armazenamento = models.IntegerField(null=True, blank=True)
    conectividade = models.BooleanField(default=False)

    def __str__(self):
        return self.nome

class Tipos(models.Model):
    unique_id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.nome