from pymongo import MongoClient
from pymongo.server_api import ServerApi

# Conexão com o MongoDB Atlas
client = MongoClient(
    "mongodb+srv://admin:admin@cluster0.chxornv.mongodb.net/",
    server_api=ServerApi('1')
)

# Selecionar o banco de dados
db = client["test"]

# Função para exibir documentos de qualquer coleção
def mostrar_documentos(nome_colecao):
    colecao = db[nome_colecao]
    documentos = list(colecao.find({}))

    if documentos:
        print(f"\n=== Documentos da coleção '{nome_colecao}' ===\n")
        for doc in documentos:
            for chave, valor in doc.items():
                print(f"{chave}: {valor}")
            print("-" * 30)
    else:
        print(f"\nA coleção '{nome_colecao}' está vazia.")

# Menu interativo
def exibir_menu():
    print("\n========= MENU =========")
    print("1 - Exibir jogadores (players)")
    print("2 - Exibir cartas (cards)")
    print("3 - Exibir batalhas (battles)")
    print("0 - Sair")
    print("========================")

# Loop principal
while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        mostrar_documentos("players")
    elif opcao == "2":
        mostrar_documentos("cards")
    elif opcao == "3":
        mostrar_documentos("battles")
    elif opcao == "0":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")
