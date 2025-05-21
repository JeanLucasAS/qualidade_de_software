# main.py

from pymongo import MongoClient
from pymongo.server_api import ServerApi

# Conexão com o MongoDB Atlas
client = MongoClient(
    API_KEY,
    server_api=ServerApi('1')
)

# Selecionar o banco de dados
db = client["test"]

def mostrar_documentos(nome_colecao):
    colecao = db[nome_colecao]
    documentos = list(colecao.find({}))
    
    resultado = []

    if documentos:
        for doc in documentos:
            item_formatado = {chave: valor for chave, valor in doc.items()}
            resultado.append(item_formatado)
    return resultado
