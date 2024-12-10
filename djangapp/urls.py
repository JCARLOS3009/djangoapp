# djangapp/urls.py
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),  # URL para o painel admin do Django
    path('pessoas/', include('pessoas.urls')),  # URL para o app pessoas
    path('', lambda request: redirect('lista_pessoas')),  # Redireciona para lista de pessoas
]
