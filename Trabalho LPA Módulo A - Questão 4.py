print("Bem vindo a Livraria do Gabriel Fontoura")
print("-" * 50)
print("-" * 15, "MENU PRINCIPAL", "-" * 19)

lista_livro = []
id_global = 0


def cadastrar_livro(id):
    global lista_livro
    print("-" * 50)
    print("-" * 13, "MENU CADASTRAR LIVRO", "-" * 15)
    nome = input("Por favor entre com o nome do livro: ")
    autor = input("Por favor entre como nome do autor: ")
    editora = input("Por favor entre com a editora do livro: ")

    livro = {
        'id': id,
        'nome': nome,
        'autor': autor,
        'editora': editora
    }

    lista_livro.append(livro)
    print(f"-" * 50)

def consultar_livro(): 
        while True:
            print("-" * 50)
            print("-" * 15, "MENU CONSULTAR LIVRO", "-" * 13)
            consulta = int(input(
                "Escolha a opção desejada:\n"
                "1 - Consultar todos os livros\n"
                "2 - Consultar Livro por id\n"
                "3 - Consultar Livro(s) por autor\n"
                "4 - Retornar\n"
            ))
            
            if consulta == 1:
                for livro in lista_livro:
                    print(f"\nID: {livro['id']}")
                    print(f"Nome: {livro['nome']}")
                    print(f"Autor: {livro['autor']}")
                    print(f"Editora: {livro['editora']}")
                    print("-" * 30)
            
            elif consulta == 2:
                id_consulta = int(input("Digite o id do livro: "))
                for livro in lista_livro:
                    if livro['id'] == id_consulta:
                        print(f"\nID: {livro['id']}")
                        print(f"Nome: {livro['nome']}")
                        print(f"Autor: {livro['autor']}")
                        print(f"Editora: {livro['editora']}")
                        break
                else:
                    print("Livro não encontrado.")
            
            elif consulta == 3:
                autor_consulta = input("Digite o autor do(s) livro(s): ").lower()
                encontrados = False
                for livro in lista_livro:
                    if autor_consulta in livro['autor'].lower():
                        print(f"\nID: {livro['id']}")
                        print(f"Nome: {livro['nome']}")
                        print(f"Autor: {livro['autor']}")
                        print(f"Editora: {livro['editora']}")
                        print("-" * 30)
                        encontrados = True
                if not encontrados:
                    print("Nenhum livro encontrado para esse autor.\n")
            
            elif consulta == 4:
                break
            
            else:
                print("Opção inválida.\n")

while True: 
    try: 
        opcao = int(input("Escolha a opção desejada:\n1 - Cadastrar Livro\n2 - Consultar Livro(s)\n3 - Remover Livro\n4 - Sair\n"))

        if opcao == 1:
            id_global += 1
            cadastrar_livro(id_global)
            
        elif opcao == 2:
            consultar_livro()

        elif opcao == 4:
            break
        else:
            print("Opção inválida.\n")
    except: 
        print("Opção Inválida. Digite apenas números.\n")
            