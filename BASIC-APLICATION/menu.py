import os
import user
import empresa

def menu():
    while True:
        nome_logo = '\033[1;34mCRAJUBAR360\033[m'
        print("=" * 50)
        print(f"{nome_logo:^60}")
        print("=" * 50)
        print("1 - EMPRESA \n2 - VIAJANTE \n3 - SAIR")
        opcao = int(input("\033[1;34mDigite a opção desejada:\033[m "))

        if opcao == 1:
            limpar_menu()
            empresa.menu_empresa_cadastro()
        elif opcao == 2:
            limpar_menu()
            user.menu_user()
        elif opcao == 3:
            print("Tchau tchau!")
            break
        else:
            limpar_menu()
            print("Opção inválida! Tente novamente.")

def limpar_menu():
    return os.system('cls' if os.name == 'nt' else 'clear')

menu()
