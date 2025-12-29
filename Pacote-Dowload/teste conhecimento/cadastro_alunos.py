from modulacao.funcao import menu
from modulacao.funcao import cadastrar_aluno
from modulacao.funcao import listar_alunos
from modulacao.funcao import sortear_aluno
from modulacao.funcao import remover_aluno

while True:
        opcao = menu()
        if opcao == "1":
            cadastrar_aluno()
        elif opcao == "2":
            listar_alunos()
        elif opcao == "3":
            sortear_aluno()
        elif opcao =="4":
            remover_aluno()
        elif opcao == "5":
            print("Encerrando o programa.")
            break
        else:
            print("Opção Invalida, Tente Novamente!!!")
            





    
    




