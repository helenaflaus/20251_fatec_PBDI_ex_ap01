import calculadora

def menu():
    while True:
        print("Escolha uma opção:")
        print("1. Somar")
        print("2. Subtrair")
        print("3. Multiplicar")
        print("4. Dividir")
        print("0. Sair")

        opcao = input("Digite a opção desejada: ")

        if opcao == "0":
            print("Saindo...")
            break
        elif opcao in ["1", "2", "3", "4"]:
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))

            if opcao == "1":
                print(f"Resultado: {calculadora.somar(a, b)}")
            elif opcao == "2":
                print(f"Resultado: {calculadora.subtrair(a, b)}")
            elif opcao == "3":
                print(f"Resultado: {calculadora.multiplicar(a, b)}")
            elif opcao == "4":
                if b != 0:
                    print(f"Resultado: {calculadora.dividir(a, b)}")
                else:
                    print("Erro: divisão por zero!")
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    menu()
