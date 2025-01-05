import os

general_list = []
toDoList = []
doneList = []

def menu_toDoList():
    print("------------------------------")
    try:
        escolha = int(input("Insira a opção desejada: \n0 - Incluir Nova Atividade \n1 - Completar Atividade \n2 - Atividades Listadas \n3 - Atividades Feitas \n4 - Excluir Atividade \n5 - Sair\n------------------------------ \nOpção: "))
        while escolha != 5:
            if escolha == 0:
                incluirAtividade()
            elif escolha == 1:
                completarAtividade()
            elif escolha == 2:
                atividadesInseridas()
            elif escolha == 3:
                atividadesFeitas()
            elif escolha == 4:
                excluirAtividade()
            elif escolha == 5:
                #saindo()
                break
            else:
                os.system("cls")
                print("------------------------------")
                print("ERRO: Informe uma opção válida")
                print("------------------------------")
                menu_toDoList()
            saindo()
            break
    except:
        os.system("cls")
        print("------------------------------")
        print("ERRO: Informe uma opção válida")
        print("------------------------------")
        menu_toDoList()

def incluirAtividade():
    os.system("cls")
    incluir_atividade = input("Insira o nome da atividade: ")
    toDoList.append("{}".format(incluir_atividade))
    general_list.append("{}".format(incluir_atividade))
    if toDoList != []:
        print("Atividade incluída com sucesso")            
    print(general_list[-1])
    menu_toDoList()

def completarAtividade():
    os.system("cls")
    if len(toDoList) == 0:
        print("Lista de atividades está vazia. Inclua uma atividade para completá-la")
        menu_toDoList
    else:
        i = 0
        while i < len(toDoList):
            print("{} - {}".format(i,toDoList[i]))
            i+=1
        try:
            completar_atividade = int(input("Informe a atividade a ser completada: "))
            completar_SN = int(input("A atividade {}, será completada! \nPressione 1 para completar e 2 para voltar: ".format((toDoList[completar_atividade]))))
            if completar_SN == 1:
                doneList.append(toDoList[completar_atividade])
                toDoList.pop(completar_atividade)
            if completar_SN == 2:
                menu_toDoList()
        except:
            completarAtividade()
            print("Informe uma opção válida")
            for i in toDoList:
                print("{}".format(i))
    menu_toDoList()

def atividadesInseridas():
    os.system("cls")
    print("As atividades inseridas até o momento foram: ")
    for i in general_list:
        print(i)    
    menu_toDoList()

def atividadesFeitas():
    os.system("cls")
    if len(doneList) == 0:
        print("Nenhuma atividade foi completada, complete alguma atividade para aparecer aqui.")
        menu_toDoList()
    else:
        print("As atividade finalizadas foram:")
        for i in doneList:
            print(i)
        menu_toDoList()

def excluirAtividade():
    os.system("cls")
    try:
        if len(toDoList) == 0:
            print("Não há nenhuma atividade a ser excluída.")
        else:
            i = 0
            while i < len(toDoList):
                print("{} - {}".format(i,toDoList[i]))
                i+=1
            excluir_atividade = int(input("Informe a atividade a ser completada: "))
            excluir_SN = int(input("A atividade {}, será excluída! \nPressione 1 para completar e 2 para voltar: ".format((toDoList[excluir_atividade]))))
            if excluir_SN == 1:
                toDoList.pop(excluir_atividade)
            if excluir_SN == 2:
                menu_toDoList()
    except:
        print("Informe uma opção válida")
    menu_toDoList()

def saindo():
    os.system("cls")
    print("Opção 5 escolhida. \nSaindo do app...")
    
    

menu_toDoList()

