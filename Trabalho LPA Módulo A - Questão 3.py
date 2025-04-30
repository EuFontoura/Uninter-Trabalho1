# Serviço de digitalização (DIG) - R$1,10
# Impressão Colorida (ICO) - R$1,00
# Impressão Preto e Branco (IPB) - R$0,40
# Fotocópia (FOT) - R$0,20

# < 20 sem desconto
# >= 20 < 200 desconto 15%
# >= 200 < 2000 desconto 20%
# >= 2000 < 20000 desconto 25%
# >= 20000 não será aceito esse número de páginas

# encadernação simples +R$15,00
# encadernação capa dura +R$40,00
# Nenhum adicional R$0,00

# total = (serviço * num_pagina) + extra

print("Bem vindo a Copiadora do Gabriel Fontoura")
def escolha_serviço():
    while True:
        selecao = input("Entre com o tipo de serviço desejado\nDIG - Digitalização\nICO - Impressão Colorida\nIPB - Impressão Preto e Branco\nFOT - Fotocópia\n").lower()

        if selecao not in ["dig", "ico", "ipb", "fot"]:
            print("Escolha inválida, entre com o tipo de serviço novamente\n")
            continue
        elif selecao == "dig":
            valor_un = 1.1
        elif selecao == "ico":
            valor_un = 1
        elif selecao == "ipb":
            valor_un = 0.4
        elif selecao == "fot":
            valor_un = 0.2
            
        while True:
            try:
                num_pag = int(input("Entre com o número de páginas: "))
                if num_pag < 20:
                    desconto = 0
                    break
                elif num_pag >= 20 and num_pag < 200:
                    desconto = 0.15
                    break
                elif num_pag >= 200 and num_pag < 2000:
                    desconto = 0.20
                    break
                elif num_pag >= 2000 and num_pag < 20000:
                    desconto = 0.25
                    break
                elif num_pag >= 20000:
                    print("Não aceitamos tantas páginas de uma vez.")
                    print("Por favor, entre com o número de páginas novamente.\n")
                    continue
            except:
                    print("Valor inválido, por favor, digite um número inteiro.")
                    continue

        while True:
            try:
                opcao_adicional = int(input("Deseja adicionar algum serviço?\n1 - Encadernação Simples - R$ 15.00\n2 - Encadernação Capa Dura  - R$ 40.00\n0 - Não desejo mais nada\n"))
                if opcao_adicional == 1:
                    adicional = 15
                    break
                elif opcao_adicional == 2:
                    adicional = 40
                    break
                elif opcao_adicional == 0:
                    adicional = 0
                    break
                else:
                    print("Opção inválida. Por favor, tente novamente.\n")
                    continue
            except:
                print("Digite apenas números (0, 1 ou 2).\n")

        total_sem_desconto = valor_un * num_pag + adicional
        total_com_desconto = total_sem_desconto * (1 - desconto)
        return(f"Total: R${total_com_desconto:.2f} (serviço: {valor_un:.2f} * páginas: {num_pag} + extra: R${adicional:.2f})")

print(escolha_serviço())