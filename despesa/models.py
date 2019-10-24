from django.db import models


# Create your models here.
class Despesa(models.Model):
    data_criacao = models.DateField("Data da criação")
    tipo_despesa = models.CharField("Tipo de depesa", )
    DESPESA_CHOICES = [
        ('remedio','Remédio'),
        ('roupa','Roupa'),
        ('alimentacao','Alimentação'),
        ('educacao','Educação'),
        ('transporte','Transporte'),
        ('outros','Outros')
    ]
    tipo_despesa = models.CharField("Tipo de despesa",max_length=20,choices=DESPESA_CHOICES)
    descricao = models.TextField("Descrição")
    FORMA_PAGAMENTO_CHOICES = [
        ('dinheiro','Dinheiro'),
        ('cartaoCredito','Cartão de crédito'),
        ('cartaoDebito','Cartão de débito'),
        ('cartaoCrediario','Cartão crediário'),
        ('cheque','Cheque')
    ]
    formaDePagamento = models.CharField("Forma de pagamento",max_length=20,choices=FORMA_PAGAMENTO_CHOICES)
    vencimento = models.DateField("Vencimento")
    quitado = models.BooleanField()
    def __str__(self):
        return "%s %s %s"%(self.descricao,
                        self.data_criacao.strftime("%d/%M/%Y"),
                        self.tipo_despesa                  
        )
    
    class Meta:
        verbose_name = "despesa"
        verbose_name_plural = "despesas"
ordering =('vencimento','formaDePagamento')
