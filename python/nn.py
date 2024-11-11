'''def lista_numeros_pares(lista:list):
    for numero in lista:
        if numero % 2 == 0:
            print(numero)

input=[1,2,3,4,5]

'''

'''def boas_vinddas(nome):
    print(f"Olá, {nome}! Seja bem-vindo(a)!")

boas_vinddas("João")'''
'''def saudacao_horario():
    try:
        hora = int(input("Digite a hora atual (0-23): "))
        
        if 6 <= hora < 12:
            print("Bom dia!")
        elif 12 <= hora < 18:
            print("Boa tarde!")
        elif (18 <= hora < 24) or (0 <= hora < 6):
            print("Boa noite!")
        else:
            print("Horário inválido. Insira uma hora entre 0 e 23.")
    except ValueError:
        print("Por favor, insira um número inteiro para a hora.")

# Exemplo de uso
saudacao_horario()'''
'''def soma(n1, n2):
    return n1 + n2

# Exemplo de uso
resultado = soma(3, 5)
print("A soma é:", resultado)'''
'''def multiplicacao(n1, n2):
    return n1 * n2

# Exemplo de uso
resultado = multiplicacao(3, 5)
print("A soma é:", resultado)'''

'''def subtracao(n1,n2):
    return n1 - n2
resultado = subtracao(10 , 3)
print("A subtração é:", resultado)'''






















'''def soma(n1, n2):
    return n1 + n2
def subtracao(n1,n2):
    return n1 - n2
def multiplicacao(n1, n2):
    return n1 * n2
def divisao(n1,n2):
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
        opcao = input("Digite a opção desejada:")
        if opcao == "5":
            print("Até logo!")
            break
        if opcao in ("1", "2", "3", "4"):
            try:                       
                n1 = float(input("Digite o primeiro número:"))
                n2 = float(input("Digite o segundo número:"))
            except ValueError:
                print("Erro! Por favor, digite um número válido.")
                continue
            if opcao == "1": 
                resultado = soma(n1,n2)

                print ("Resultado da soma", resultado)
            elif opcao == '2':
                resultado = subtracao(n1,n2)
                print ("Resultado da subtração", resultado)
            elif opcao == '3':
                resultado = multiplicacao(n1,n2)
                print ("Resultado da multiplicação", resultado) 
            elif opcao == '4':
                if n2 == 0: 
                    print("Erro! Não é possível dividir por zero.")
        else:
            print("Opção invalida")
            
calculadora()'''
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