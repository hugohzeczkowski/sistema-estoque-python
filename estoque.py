estoque = {}
while True:
    print("\n Selecione uma opção:")
    print("1 - Adicionar item")
    print("2 - Excluir item")
    print("3 - Editar item")
    print("4 - Mostrar estoque")
    print("5 - Sair")

    opcao = input("Digite a opção: ")
    if opcao == "1":
        produto = input("Produto: ").strip().lower()
        if not produto:
            print("Sem produto inserido.")
            continue
        if produto.isdigit():
            print("O nome produto precisar sem em texto")
            continue
        try:
            preco = float(input("Preço do produto: "))
            if preco <= 0:
                print("Preço deve ser maior que zero.")
                continue
        except ValueError:
            print("Preço inválido.")
            continue

        try:
            quantidade = int(input("Digite a quantidade: "))
            if quantidade <= 0:
                print("Quantidade deve ser maior que zero.")
                continue
        except ValueError:
            print("Quantidade inválida.")
            continue
        if produto in estoque:
            print("Esse produto já existe no estoque")
            continue    
        estoque[produto] = {
            "preço": preco,
            "quantidade": quantidade
        }
        print("Produto adicionado com sucesso!")
    elif opcao == "2":
        produto_excluir = input("Qual produto você quer excluir: ").strip().lower()
        if produto_excluir in estoque:
            del estoque[produto_excluir]
            print("O produto foi excluido com sucesso")
        else:
            print("O produto não existe no estoque!")
    elif opcao == "3":
        editar_produto = input("Qual é o produto que você deseja editar? ").strip().lower()
        if editar_produto in estoque:
            dados = estoque[editar_produto]
            print ("O preço atual é:", dados["preco"])
            print ("A quantidade atual é:", dados["quantidade"])
            try:
                preco_novo = float(input("Novo preço do produto: ")).strip()
                if preco_novo <= 0:
                    print("Preço deve ser maior que zero.")
            except ValueError:
                print("Preço inválido.")
            try:
                quantidade_nova = float(input("Nova quantidade do produto: ")).strip()
                if quantidade_nova <= 0:
                    print("A quantidade deve ser maior que zero.")
            except ValueError:
                print("Quantidade inválida.")
            estoque[editar_produto] = {
                "preco": preco_novo,
                "quantidade": quantidade_nova
        }
        else:
            print("Esse produto não existe no estoque!")
    elif opcao == "4":
        if not estoque: 
            print("Não há nada no estoque")
        
        else:
            for produto in estoque:
                print ("Nome:", produto.title(), "Quantidade:", estoque[produto]["quantidade"])
    elif opcao == "5":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Digite um número inteiro (ex: 1, 2...)")