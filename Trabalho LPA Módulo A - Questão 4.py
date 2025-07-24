print("Bem vindo a Livraria do Gabriel Fontoura")
print("-" * 50)
print("-" * 15, "MENU PRINCIPAL", "-" * 19)

lista_livro = []
id_global = 0

# Função de cadastrar livro
def cadastrar_livro(id):
    """Cadastra um novo livro na lista livro

    Args:
        id (int): Identificador único do livro, gerado automáticamente sempre que a opção de "cadastrar livro" é selecionada, com base na variável global id_global

        A função solicita ao usuário o nome, autor e editora do livro, cria um dicionário com as informações e adiciona na lista_livro.
    """
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

# Funçao de consultar livro
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
                # formatação da biblioteca (o padrão se repete para cada consulta)
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

def remover_livro():
    while True:
        id_remover = int(input("Digite o ID do livro que deseja remover: "))
        for livro in lista_livro:
            if livro['id'] == id_remover:
                lista_livro.remove(livro)
                print(f"Livro removido com sucesso!\n")
                return
        print("ID inválido. Tente novamente.")

# chamando as funções
while True: 
    try: 
        opcao = int(input("Escolha a opção desejada:\n1 - Cadastrar Livro\n2 - Consultar Livro(s)\n3 - Remover Livro\n4 - Sair\n"))

        if opcao == 1:
            id_global += 1
            cadastrar_livro(id_global)
            
        elif opcao == 2:
            consultar_livro()

        elif opcao == 3: 
            remover_livro()

        elif opcao == 4:
            break
        else:
            print("Opção inválida.\n")
    except: 
        print("Opção Inválida. Digite apenas números.\n")
            