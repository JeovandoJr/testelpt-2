def soma (valor1, valor2):
    return valor1 + valor2

def subtrai (valor1, valor2):
    return valor1 - valor2

def multiplica (valor1 , valor2):
    return valor1 * valor2

def divide (valor1, valor2):
    if valor2 == 0:
        print("Não é possível dividir.")
    return valor1 / valor2

def menu ():
    print("1. Soma")
    print("2. Subtrai")
    print("3. Multiplica")
    print("4. Divide")
    print("5. Sair")


while True:
    menu()
    print("Digite os valores:")
    valor1 = float(input("Digite o valor 1: "))
    valor2 = float(input("Digite o valor 2: "))

    opcao = input("Qual a opção de operação? ")

    if opcao == "1":
        resultado = soma(valor1, valor2)
        print(f"Resultado da Soma: {resultado}\n")

    elif opcao == "2":
        resultado = subtrai(valor1, valor2)
        print(f"Resultado da Subtração: {resultado}\n")
    
    elif opcao == "3":
        resultado = multiplica(valor1, valor2)
        print(f"Resultado da Multiplicação: {resultado}\n")

    elif opcao == "4":
        resultado = divide(valor1, valor2)
        print(f"Resultado da Divisão: {resultado}\n")
    
    elif opcao == "5":
        break

    else:
        print("Opção Inválida.\n")
    