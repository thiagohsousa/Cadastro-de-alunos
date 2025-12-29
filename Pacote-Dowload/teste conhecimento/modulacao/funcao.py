import random

alunos = []

def menu():
    print("""--------------------------------------
    C A D A S T R O   D E   A L U N O S
    --------------------------------------
    
    1 - Cadastrar novo aluno
    2 - Listar Alunos
    3 - Sortear Aluno
    4 - Remover Aluno
    5 - Sair
--------------------------------------""")
          
    opcao = input("Escolha uma opção: ")
    return opcao

def cadastrar_aluno():
   try:
    nome = input("Digite o nome do aluno: ")
    cpf = int (input("Digite o CPF do aluno: "))
    idade = int( input("Digite a idade do aluno: "))
    alunos.append((nome, cpf, idade))
    print("Aluno cadastrado com sucesso!\n")
   except ValueError:
       print("idade ou cpf invalidos, tente novamente")

def listar_alunos():
    if not alunos:
        print("Nenhum aluno cadastrado ainda.\n")
    else:
        print("\nLista de Alunos:")
        for i, aluno in enumerate(alunos, start=1):
            nome, cpf, idade = aluno
            print(f"{i}. Nome: {nome}, CPF: {cpf}, Idade: {idade}")
        print()


def sortear_aluno():
    if alunos:
        sorteado = random.choice(alunos)
        print(f"Aluno sorteado: {sorteado[0]} (CPF: {sorteado[1]}, Idade: {sorteado[2]})\n")
    else:
        print("Não há alunos para sortear.\n")


def remover_aluno():
    if not alunos:
        print("Não há alunos cadastrados no sistema.\n")
        return

    listar_alunos()
    try:
        opcao = int(input("Digite o número do aluno que deseja remover: "))
        if 1 <= opcao <= len(alunos):
            removido = alunos.pop(opcao - 1)
            print(f"Aluno {removido[0]} removido com sucesso!\n")
        else:
            print("Número inválido!\n")
    except ValueError:
        print("Digite um número válido.\n")

            
    
       



   


