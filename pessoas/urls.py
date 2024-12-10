# pessoas/urls.py
from django.urls import path
from . import views  # Importando as views do app pessoas

urlpatterns = [
    path('', views.lista_pessoas, name='lista_pessoas'),  # Página para listar as pessoas
    path('nova/', views.cria_pessoa, name='cria_pessoa'),  # Página para criar uma nova pessoa
    path('editar/<int:pk>/', views.edita_pessoa, name='edita_pessoa'),  # Página para editar pessoa
    path('deletar/<int:pk>/', views.deleta_pessoa, name='deleta_pessoa'),  # Página para deletar pessoa
]
