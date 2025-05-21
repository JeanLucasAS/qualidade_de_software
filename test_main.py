# test_main.py

import pytest
from main import mostrar_documentos

# Testar se retorna uma lista
def test_mostrar_documentos_retorna_lista():
    resultado = mostrar_documentos("players")
    assert isinstance(resultado, list)

# Testar se a coleção não está vazia (supondo que você já tem dados no Mongo)
def test_mostrar_documentos_players_nao_vazio():
    resultado = mostrar_documentos("players")
    assert len(resultado) > 0

# Testar uma chave específica (supondo que tenha um campo 'nickname' nos players)
def test_mostrar_documentos_tem_chave_nickname():
    resultado = mostrar_documentos("players")
    if resultado:
        assert "nickname" in resultado[0]
