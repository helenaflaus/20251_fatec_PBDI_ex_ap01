import calculadora

def menu():
    while True:
        print("\nEscolha uma opção:")
        print("1. Somar")
        print("2. Subtrair")
        print("3. Multiplicar")
        print("4. Dividir")
        print("0. Sair")

        opcao = input("Digite a opção desejada: ")
        if opcao == "0":
            print("Saindo...")
            break
        elif opcao == "1":
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
            print(f"Resultado: {calculadora.somar(a, b)}")
        elif opcao == "2":
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
            print(f"Resultado: {calculadora.subtrair(a, b)}")
