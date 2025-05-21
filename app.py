# app.py
import argparse
from main import mostrar_documentos

def main():
    parser = argparse.ArgumentParser(description="Visualizar documentos do MongoDB...")
    parser.add_argument(
        "--colecao",
        choices=["players", "cards", "battles"],
        required=True,
        help="Nome da coleção a ser exibida."
    )
    args = parser.parse_args()

    documentos = mostrar_documentos(args.colecao)
    if documentos:
        print(f"\n=== Documentos da coleção '{args.colecao}' ===\n")
        for doc in documentos:
            for chave, valor in doc.items():
                print(f"{chave}: {valor}")
            print("-" * 30)
    else:
        print(f"\nA coleção '{args.colecao}' está vazia.")

if __name__ == "__main__":
    main()
