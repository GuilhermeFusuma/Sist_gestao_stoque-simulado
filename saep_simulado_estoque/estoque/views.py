from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request):
    return redirect('accounts/login')

@login_required
def pag_inicial(request):
    user = request.user

    return render(request, 'estoque/indexEstoque.html', {'user': user})