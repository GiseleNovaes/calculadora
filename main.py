def calculadora():
    while True:
        print("\nEscolha uma operação:")
        print("1. Adição")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair")

        escolha = input("Digite o número da operação desejada: ")

        if escolha == '5':
            print("Programa encerrado.")
            break

        if escolha in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))

                if escolha == '1':
                    resultado = num1 + num2
                    print(f"{num1} + {num2} = {resultado}")
                elif escolha == '2':
                    resultado = num1 - num2
                    print(f"{num1} - {num2} = {resultado}")
                elif escolha == '3':
                    resultado = num1 * num2
                    print(f"{num1} * {num2} = {resultado}")
                elif escolha == '4':
                    resultado = num1 / num2
                    print(f"{num1} / {num2} = {resultado}")

            except ZeroDivisionError:
                print("Erro: Divisão por zero não é permitida.")
            except ValueError:
                print("Erro: Entrada inválida. Digite apenas números.")
        else:
            print("Opção inválida. Por favor, escolha uma operação válida.")

calculadora()
