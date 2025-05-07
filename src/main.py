print("Calculadora")


num1 = float(input("Digite o primeiro número: "))

num2 = float(input("Digite o segundo número: "))

print("Escolha a operação:")
print("1 - Soma (+)")
print("2 - Subtração (-)")
print("3 - Multiplicação (*)")
print("4 - Divisão (/)")

# Pega a escolha do usuário
opcao = input("Digite o número da operação (1/2/3/4): ")

# Realiza o cálculo de acordo com a escolha
if opcao == "1":
    resultado = num1 + num2
    print("Resultado da soma:", resultado)
elif opcao == "2":
    resultado = num1 - num2
    print("Resultado da subtração:", resultado)
elif opcao == "3":
    resultado = num1 * num2
    print("Resultado da multiplicação:", resultado)
elif opcao == "4":
    if num2 != 0:
        resultado = num1 / num2
        print("Resultado da divisão:", resultado)
    else:
        print("Erro: Não é possível dividir por zero.")
else:
    print("Opção inválida.")
