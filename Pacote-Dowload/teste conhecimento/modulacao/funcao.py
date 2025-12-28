alunos = []

def menu():
    print("""--------------------------------------
    C A D A S T R O   D E   A L U N O S
    --------------------------------------
    
    1 - Cadastrar novo aluno
    2 - Listar alunos
    3 - Sortear aluno
    4 - Sair
--------------------------------------""")
          
    opcao = input("Escolha uma opção: ")
    return opcao

def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    cpf = int (input("Digite o CPF do aluno: "))
    idade = int( input("Digite a idade do aluno: "))
    alunos.append((nome, cpf, idade))
    print("Aluno cadastrado com sucesso!\n")

def listar_alunos():
    if not alunos:
        print("Nenhum aluno cadastrado ainda.\n")
    else:
        print("\nLista de Alunos:")
        for i, aluno in enumerate(alunos, start=1):
            nome, cpf, idade = aluno
            print(f"{i}. Nome: {nome}, CPF: {cpf}, Idade: {idade}")
        print()

import random
def sortear_aluno():
    if alunos:
        sorteado = random.choice(alunos)
        print(f"Aluno sorteado: {sorteado[0]} (CPF: {sorteado[1]}, Idade: {sorteado[2]})\n")
    else:
        print("Não há alunos para sortear.\n")

        



   


