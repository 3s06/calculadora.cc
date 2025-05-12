import math

print("Calculadora")
historico = []

# Variável de controle do laço infinito
rodando = True

# Laço principal da calculadora
while rodando == True:
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        #se der errado
        print("Por favor, digite números válidos.")
        continue
        #aqui ele vai continuar até tu botar o numero certinho
        #em baixo as opções dos tipos de escolha que o usuario qr fazer
    print("Escolha a operação:")
    print("1 - Soma (+)") 
    print("2 - Subtração (-)")
    print("3 - Multiplicação (*)")
    print("4 - Divisão (/)")
    print("5 - Exponenciação (^)")
    print("6 - Raiz quadrada (√)")
    print("8 - Seno (sin)")
    print("9 - Cosseno (cos)")
    print("10 - Tangente (tan)")
    print("11 - Porcentagem (%)")
    print("12 - Converter Graus para Radianos")
    print("13 - Converter Radianos para Graus")
    print("14 - Ver Histórico")

    opcao = input("Digite o número da operação (1/2/3/4/5/6/7/8/9/10/11/12/13/14): ")
            #aqui ele faz o calculo de acordo com oq ele escolheu
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
    elif opcao == "5":
        resultado = num1 ** num2
        print(f"Resultado de {num1} elevado a {num2}:", resultado)
    elif opcao == "6":
        if num1 >= 0:
            resultado = math.sqrt(num1)
            print(f"Resultado da raiz quadrada de {num1}:", resultado)
        else:
            print("Erro: Não é possível calcular a raiz quadrada de um número negativo.")
    else:
        print("Opção inválida.")
        elif opcao == "7":
        if num1.is_integer() and num1 >= 0:
            resultado = math.factorial(int(num1))
            print(f"Fatorial de {int(num1)}:", resultado)
        else:
            print("Erro: O número deve ser um inteiro positivo para calcular o fatorial.")
    elif opcao == "8":
        resultado = math.sin(math.radians(num1))  # Converte de graus para radianos
        print(f"Seno de {num1} graus:", resultado)
    elif opcao == "9":
        resultado = math.cos(math.radians(num1))  # Converte de graus para radianos
        print(f"Cosseno de {num1} graus:", resultado)
    elif opcao == "10":
        resultado = math.tan(math.radians(num1))  # Converte de graus para radianos
        print(f"Tangente de {num1} graus:", resultado)
    elif opcao == "11":
        try:
            num2 = float(input("Digite o número para calcular a porcentagem de: "))
            resultado = (num1 / 100) * num2
            print(f"{num1}% de {num2} é:", resultado)
        except ValueError:
            print("Por favor, digite um número válido para o cálculo da porcentagem.")
    elif opcao == "12":
        resultado = math.radians(num1)
        print(f"{num1} graus em radianos é:", resultado)
    elif opcao == "13":
        resultado = math.degrees(num1)
        print(f"{num1} radianos em graus é:", resultado)
    elif opcao == "14":
        print("Histórico de cálculos:")
        for h in historico:
            print(h)
    else:
        print("Opção inválida.")

    historico.append(f"Operação: {opcao} - Resultado: {resultado}")
    
    continuar = input("Deseja realizar outra operação? (sim/não): ").lower()
    if continuar != 'sim':
        rodando = False
    #ela vai começar outra operação.
