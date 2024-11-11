def soma(n1, n2):
    return n1 + n2

def subtracao(n1, n2):
    return n1 - n2

def multiplicacao(n1, n2):
    return n1 * n2

def divisao(n1, n2):
    if n2 == 0:
        return "Erro: divisão por zero"
    return n1 / n2

def menu():
    print("\nEscolha uma operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")

def calculadora():
    while True:
        menu()
        opcao = input("Digite a opção desejada: ")
        
        if opcao == '5':
            print("Saindo da calculadora...")
            break

        if opcao in ['1', '2', '3', '4']:
            try:
                n1 = float(input("Digite o primeiro número: "))
                n2 = float(input("Digite o segundo número: "))
            except ValueError:
                print("Erro: por favor, insira números válidos.")
                continue
            
            if opcao == '1':
                resultado = soma(n1, n2)
                print("Resultado da soma:", resultado)
            elif opcao == '2':
                resultado = subtracao(n1, n2)
                print("Resultado da subtração:", resultado)
            elif opcao == '3':
                resultado = multiplicacao(n1, n2)
                print("Resultado da multiplicação:", resultado)
            elif opcao == '4':
                resultado = divisao(n1, n2)
                print("Resultado da divisão:", resultado)
        else:
            print("Opção inválida! Tente novamente.")


calculadora()