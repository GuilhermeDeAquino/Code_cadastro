import database

def limpar_peso(peso):
    peso = peso.lower().replace("kg", "").replace(",", ".").strip()
    return float(peso)

database.criar_tabela()

while True:
    print("1 - Cadastrar")
    print("2 - Ver dados salvos")
    print("3 - Exportar dados para TXT")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        print("\nCadastro\n")

        nome = input("Nome: ")
        idade = int(input("Idade: "))
        sexo = input("Sexo: ")
        altura = float(input("Altura: "))
        peso = limpar_peso(input("Peso: "))

        database.inserir_usuario(nome, idade, sexo, altura, peso)

       
        database.exportar_usuarios_txt()

        print("\nUsuário cadastrado com sucesso ")
        print("Arquivo usuarios.txt atualizado automaticamente")


    elif opcao == "2":
        print("\nUsuários cadastrados:\n")

        usuarios = database.listar_usuarios()

        if not usuarios:
            print("Nenhum cadastro ainda.")
        else:
            for u in usuarios:
                print(f"ID: {u[0]} | Nome: {u[1]} | Idade: {u[2]} | Sexo: {u[3]} | Altura: {u[4]} | Peso: {u[5]}")

   
    elif opcao == "3":
        database.exportar_usuarios_txt()
        print("\nArquivo usuarios.txt gerado com sucesso \n")

    elif opcao == "0":
        print("Saindo...")
        break

    else:
        print("Opção inválida")



    
