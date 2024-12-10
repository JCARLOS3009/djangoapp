# pessoas/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Pessoa
from .forms import PessoaForm

def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'pessoas/lista_pessoas.html', {'pessoas': pessoas})

def cria_pessoa(request):
    if request.method == "POST":
        form = PessoaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_pessoas')
    else:
        form = PessoaForm()
    return render(request, 'pessoas/cria_pessoa.html', {'form': form})

def edita_pessoa(request, pk):
    pessoa = get_object_or_404(Pessoa, pk=pk)
    if request.method == "POST":
        form = PessoaForm(request.POST, instance=pessoa)
        if form.is_valid():
            form.save()
            return redirect('lista_pessoas')
    else:
        form = PessoaForm(instance=pessoa)
    return render(request, 'pessoas/edita_pessoa.html', {'form': form})

def deleta_pessoa(request, pk):
    pessoa = get_object_or_404(Pessoa, pk=pk)
    if request.method == "POST":
        pessoa.delete()
        return redirect('lista_pessoas')
    return render(request, 'pessoas/deleta_pessoa.html', {'pessoa': pessoa})
