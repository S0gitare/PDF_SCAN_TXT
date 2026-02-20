import os


while True:

    entrada = input("Caminho de Origem do PDF: ")

    if os.path.exists(entrada):

        caminho_origem = os.path.normpath(entrada).replace("\\", "\\\\")

        nome_arquivo = os.path.basename(caminho_origem)

        nome_puro = os.path.splitext(nome_arquivo)[0]

        arquivo_final = nome_puro + ".txt"

        break
    else:
        print("As pastas NÂO existem.")
