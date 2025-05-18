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
        print("Histórico de cálculos:")  # aqui é o historico
        for h in historico:
            print(h)
    else:
        print("Opção inválida.")
        elif opcao == "15":
        historico.clear()   #aqui é pra apagar historico
    print("Histórico apagado.") 
    elif opcao == "16":
    resultado = (num1 + num2) / 2
    print(f"Média entre {num1} e {num2} é:", resultado) # aqui nois mexe em media e talz
        historico.append(f"Operação: {opcao} - Resultado: {resultado}")    
        elif opcao == "17":  #aqui é pra comparação de numeros (tipo maior,menor ou igual)
    if num1 > num2:
        resultado = f"{num1} é maior que {num2}"
    elif num1 < num2:
        resultado = f"{num1} é menor que {num2}"
    else:
        resultado = "Os dois números são iguais"
    print(resultado)
elif opcao == "18":  #aqui é a calculadora da area do triangulo
    try:
        base = float(input("Digite a base do triângulo: "))
        altura = float(input("Digite a altura do triângulo: "))
        resultado = (base * altura) / 2
        print(f"Área do triângulo com base {base} e altura {altura} é:", resultado)
    except ValueError:
        print("Valores inválidos.")
elif opcao == "20":
    resultado = round(num1) # aqui é pra arredondar o numero
    print(f"{num1} arredondado é:", resultado)
elif opcao == "21":
    resultado = -num1   
    print(f"Inverso de sinal de {num1} é:", resultado) # aqui inverte uns sinais
elif opcao == "22":
    if num2 != 0 and num1 % num2 == 0:
        resultado = f"{num1} é múltiplo de {num2}"
    else:
        resultado = f"{num1} NÃO é múltiplo de {num2}"
    print(resultado) #aqui verifica se os numeros são multiplos
elif opcao == "23":
    try:
        nota1 = float(input("Digite a primeira nota: ")) #aqui fica a media ponderada 
        peso1 = float(input("Digite o peso da primeira nota: "))
        nota2 = float(input("Digite a segunda nota: "))
        peso2 = float(input("Digite o peso da segunda nota: "))
        resultado = (nota1 * peso1 + nota2 * peso2) / (peso1 + peso2)
        print("Média ponderada:", resultado)
    except ValueError:
        print("Valores inválidos.")
        elif opcao == "24":
    try:
        qtd = int(input("Quantos números deseja calcular a média? ")) # aqui faz a media de varios numeros
        soma = 0
        for i in range(qtd):
            numero = float(input(f"Digite o número {i+1}: "))
            soma += numero
        resultado = soma / qtd
        print("Média dos números:", resultado)
    except ValueError:
        print("Entrada inválida.")
elif opcao == "25":
    resultado = num1 ** (-abs(num2))  #aqui faz potencia com o expoente negativo
    print(f"{num1} elevado a -{abs(num2)} é:", resultado)
elif opcao == "26":
    if int(num1) % 2 == 0:  
        resultado = f"{int(num1)} é par"
    else:
        resultado = f"{int(num1)} é ímpar"
    print(resultado)  # aqui é so para saber se o numero é impa ou par ( kkkkkk)
elif opcao == "27":
    if num1.is_integer() and num1 > 1:
        num = int(num1)
        primo = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                primo = False
                break
        if primo:
            resultado = f"{num} é um número primo"
        else:
            resultado = f"{num} NÃO é primo"
    else:
        resultado = "Número inválido para verificação de primo"
    print(resultado) # aqui botei pra verifica se o numero é primo ou não
elif opcao == "28":
    try:
        valor_em_reais = float(input("Digite o valor em reais: R$ ")) #botei a função para a calculadora converter valores de reais pra dolar
        taxa_dolar = 5.00  
        resultado = valor_em_reais / taxa_dolar
        print(f"R$ {valor_em_reais} equivalem a US$ {resultado:.2f}")
    except ValueError:
        print("Valor inválido.")
    continuar = input("Deseja realizar outra operação? (sim/não): ").lower()
    if continuar != 'sim':
        rodando = False
    #ela vai começar outra operação.
    elif opcao == "0":
    if historico:
        print("Repetindo última operação...")
        print(historico[-1])
    else:
        print("Nenhuma operação anterior encontrada.")
        #essa parte aqui Permite repetir a ultima operação com os mesmos numeros
