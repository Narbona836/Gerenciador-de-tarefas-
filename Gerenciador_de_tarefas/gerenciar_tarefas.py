import os 


tarefas = []

def nome_do_programa():
    print("""
        Ｇｅｒｅｎｃｉａｄｏｒ ｄｅ ｔａｒｅｆａｓ
        """)

def adicionar_tarefa():
    os.system("cls")
    nova_tarefa = input("Digite a nova tarefa que deseja adicionar: \n")
    tarefas.append(nova_tarefa)
    print(f"Tarefa '{nova_tarefa}' adicionada com sucesso.\n")
    voltar_ao_menu_principal()

def visualizar_tarefas():
    os.system("cls")
    if not tarefas:
        print("Nenhuma tarefa na lista!\n")
        exibir_opcoes()
    else:
        print(f"Tarefas na lista: -->  {list(enumerate(tarefas, 1))}\n")
        voltar_ao_menu_principal()

def remover_tarefa():
    os.system("cls")
    if not tarefas:
        print("Nenhuma tarefa na lista!\n")
        exibir_opcoes()
    else:
        print(f"Tarefas na lista: -->  {list(enumerate(tarefas, 1))}\n")
        try:
            indice = int(input("Digite o número da tarefa que deseja remover: \n")) - 1
            if 0 <= indice < len(tarefas):
                tarefa_removida = tarefas.pop(indice)
                print(f"Tarefa '{tarefa_removida}' removida com sucesso.\n")
                exibir_opcoes()
            else:
                print("Índice inválido.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.\n")
            voltar_ao_menu_principal()

def finalizar_app():
    os.system("cls")
    print("Finalizando o programa...\n")
    exit()

def voltar_ao_menu_principal():
    input("Pressione uma tecla para voltar ao menu principal ")
    os.system("cls")
    exibir_opcoes()

def exibir_opcoes():
    print("1. Adicionar uma tarefa")
    print("2. Visualizar lista de tarefas")
    print("3. Remover uma tarefa da lista")
    print("4. Sair do programa\n")

def gerenciador_de_tarefas():
    while True:
        exibir_opcoes()
    
        try:
            while True:
                nova_tarefa = input("Digite a opção desejada: ")
                if nova_tarefa not in ["1", "2", "3", "4"]:
                    os.system("cls")
                    print("Opção inválida. Tente a opção 1,2,3 ou 4.\n")
                    continue
                if nova_tarefa == "1":
                    adicionar_tarefa()

                elif nova_tarefa == "2":
                    visualizar_tarefas()

                elif nova_tarefa == "3":
                    remover_tarefa()
                else:
                    finalizar_app()
                    break
                
        except ValueError:
            os.system("cls")
            print("Entrada inválida. Por favor, insira um número.\n")
            continue

def main():
    nome_do_programa()
    gerenciador_de_tarefas()
    visualizar_tarefas()

if __name__ == "__main__":
    main()