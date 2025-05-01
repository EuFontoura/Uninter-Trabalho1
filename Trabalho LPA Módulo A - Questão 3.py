
print("Bem vindo a Copiadora do Gabriel Fontoura")

# Função para o tipo de serviço
def escolha_serviço():
    while True:
        selecao = input("Entre com o tipo de serviço desejado\nDIG - Digitalização\nICO - Impressão Colorida\nIPB - Impressão Preto e Branco\nFOT - Fotocópia\n").lower()

        if selecao not in ["dig", "ico", "ipb", "fot"]:
            print("Escolha inválida, entre com o tipo de serviço novamente\n")
            continue
        elif selecao == "dig":
            return 1.1
        elif selecao == "ico":
            return 1
        elif selecao == "ipb":
            return 0.4
        elif selecao == "fot":
            return 0.2

# Função para informar número de páginas 
def num_pagina():
    while True:
        try:
            num_pag = int(input("Entre com o número de páginas: "))
            if num_pag < 20:
                return num_pag, 0

            elif num_pag >= 20 and num_pag < 200:
                return num_pag, 0.15

            elif num_pag >= 200 and num_pag < 2000:
                return num_pag, 0.20

            elif num_pag >= 2000 and num_pag < 20000:
                return num_pag, 0.25

            elif num_pag >= 20000:
                print("Não aceitamos tantas páginas de uma vez.")
                print("Por favor, entre com o número de páginas novamente.\n")

        except:
                print("Valor inválido, por favor, digite um número inteiro.")

# Função para escolher serviço adicional
def servico_extra():
    while True:
        try:
            opcao_adicional = int(input("Deseja adicionar algum serviço?\n1 - Encadernação Simples - R$ 15.00\n2 - Encadernação Capa Dura  - R$ 40.00\n0 - Não desejo mais nada\n"))
            if opcao_adicional == 1:
                return 15

            elif opcao_adicional == 2:
                return 40

            elif opcao_adicional == 0:
                return 0

            else:
                print("Opção inválida. Por favor, tente novamente.\n")

        except:
            print("Digite apenas números (0, 1 ou 2).\n")


# código principal
valor_un = escolha_serviço()
num_pag, desconto = num_pagina()
adicional = servico_extra()

# aplicando desconto no total de páginas
valor_pagina_com_desconto = int(num_pag - (num_pag * desconto))
total_com_desconto = (valor_un * valor_pagina_com_desconto) + adicional

# resultado final
print(f"Total: R${total_com_desconto:.2f} (serviço: {valor_un:.2f} * páginas: {valor_pagina_com_desconto} + extra: R${adicional:.2f})")