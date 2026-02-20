import os
import fitz


def converter(caminho_origem, arquivo_final):
    print(f"Convertendo {caminho_origem} para {arquivo_final}")

    with fitz.open(caminho_origem) as pdf:
        with open(arquivo_final, "w", encoding="utf-8") as txt:
            for i in range(len(pdf)):
                pagina = pdf[i]
                print(f"Processando página {i + 1} de {len(pdf)}...", end="\r")
                texto = pagina.get_text()
                txt.write(str(texto))
                txt.write("\n" + "-" * 20 + "\n")


def main():
    while True:
        entrada = input("Caminho de Origem do PDF: ").strip().strip('"')
        caminho_origem = os.path.abspath(entrada)

        if os.path.isfile(caminho_origem):
            diretorio = os.path.dirname(caminho_origem)
            nome_puro = os.path.splitext(os.path.basename(caminho_origem))[0]
            arquivo_final = os.path.join(diretorio, nome_puro + ".txt")

            converter(caminho_origem, arquivo_final)
            break
        else:
            print(f"ERRO: O arquivo '{caminho_origem}' não existe.")


if __name__ == "__main__":
    main()
