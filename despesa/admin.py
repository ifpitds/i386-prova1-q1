from django.contrib import admin
from .models import Despesa
# Register your models here.

class DespesaAdmin(admin.ModelAdmin):
    list_display = ('data_criacao','tipo_despesa',
                    'descricao','formaDePagamento',
                    'vencimento','proximoVencimento','quitado',
    )

    list_filter = ('quitado','vencimento')
    date_hierarchy = ('vencimento')

    
    def proximoVencimento(self, obj):
        return True

    proximoVencimento.short_description = "Próximo ao vencimento?"
    proximoVencimento.boolean = True
    
admin.site.register(Despesa, DespesaAdmin)
admin.site.site_header = "Controle de despesas"
admin.site.index_title = "Recursos"
admin.site.site_title = "Administração das despesas"
