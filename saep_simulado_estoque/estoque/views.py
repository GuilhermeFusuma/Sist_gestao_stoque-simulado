from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from .models import Equipamentos, Movimentacoes

# Create your views here.
def login(request):
    return redirect('accounts/login')

@login_required
def pag_inicial(request):
    user = request.user

    return render(request, 'estoque/indexEstoque.html', {'user': user})

@login_required
def gestao_estoque(request):
    produtos = Equipamentos.objects.all().order_by('nome') 
    
    entradas_qs = Movimentacoes.objects.filter(
        tipo_operacao__iexact='entrada' 
    ).values('equipamento').annotate(
        soma_entradas=Sum('quantidade')
    )
    
    saidas_qs = Movimentacoes.objects.filter(
        tipo_operacao__iexact='saida'
    ).values('equipamento').annotate(
        soma_saidas=Sum('quantidade')
    )
    
    entradas_dict = {item['equipamento']: item['soma_entradas'] for item in entradas_qs}
    saidas_dict = {item['equipamento']: item['soma_saidas'] for item in saidas_qs}
    
    for produto in produtos:
        produto.total_entradas = entradas_dict.get(produto.pk, 0)
        produto.total_saidas = saidas_dict.get(produto.pk, 0)
        
        produto.saldo_atual = produto.total_entradas - produto.total_saidas
        
    context = {
        "produtos": produtos,
    }

    return render(request, 'estoque/gestaoProdutos.html', context)