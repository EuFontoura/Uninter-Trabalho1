print("Bem vindo a Livraria do Gabriel Fontoura")
print("-" * 50)
print("-" * 15, "MENU PRINCIPAL", "-" * 19)
opcao = input("Escolha a opção desejada:\n1 - Cadastrar Livro\n2 - Consultar Livro(s)\n3 - Remover Livro\n4 - Sair\n")

lista_livro = []
id_global = 0

def cadastrar_livro(id):
    nome = input("Por favor entre com o nome do livro: ")
    autor = input("Por favor entre como nome do autor: ")
    editora = input("Por favor entre com a editora do livro: ")