import math #botei isso pq ele importa o módulo 'math' que possui funções matematicas avançadas como seno,cosseno,fatorial etc.

print("Calculadora") #isso aqui é so a mensagem inicial kk
historico = [] #aqui botei a lista para armazenar o historico das operações realizadas durante o uso da calculadora

# Variável de controle do laço infinito 
rodando = True 

# Laço principal da calculadora
while rodando == True:
    try: #aqui tu botaria dois numeros principais que todas as operações vão usar para calcular
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        #se der errado, tipo ele digita algo não numero, dai ele toma erro.
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
    print("15- apagar histórico")
    print("16 - Média entre dois números")
    print("17 - Comparar dois números")
    print("18 - Área do triângulo")
    print("19 - Arredondar número") 
    print("20 - Inverter sinal")    
    print("21 - Verificar múltiplo")    
    print("22 - Média ponderada")   
    print("23 - Média de vários números")       
    print("24 - Potência com expoente negativo")    
    print("25 - Verificar par ou ímpar")
    print("26 - Verificar número primo")    
    print("27 - Converter Reais para Dólares")
    print("0 - Repetir última operação")        
    opcao = input("Digite o número da operação (1/2/3/4/5/6/7/8/9/10/11/12/13/14/15/16/17/18/19/20/21/22/23/24/25/26/27/0): ")
            #aqui ele faz o calculo de acordo com oq ele escolheu
    #soma dos dois numeros (num1 + num2)
    if opcao == "1":
        resultado = num1 + num2
        print("Resultado da soma:", resultado)
    #subtração dos dois numeros (num1 - num2)    
    elif opcao == "2":
        resultado = num1 - num2
        print("Resultado da subtração:", resultado)
    #multiplicação dos dois numeros (num1 * num2)
    elif opcao == "3":
        resultado = num1 * num2
        print("Resultado da multiplicação:", resultado)
    # divisão dos dois numeros (num1 / num2)    
    elif opcao == "4":
        if num2 != 0:
            resultado = num1 / num2
            print("Resultado da divisão:", resultado)
        else:
            print("Erro: Não é possível dividir por zero.")
    # exponenciação dos dois numeros (num1 ** num2)
    elif opcao == "5":
        resultado = num1 ** num2
        print(f"Resultado de {num1} elevado a {num2}:", resultado)
    # raiz quadrada do primeiro numero (num1)
    elif opcao == "6":
        if num1 >= 0:
            resultado = math.sqrt(num1)
            print(f"Resultado da raiz quadrada de {num1}:", resultado)
        else:
            print("Erro: Não é possível calcular a raiz quadrada de um número negativo.")
    else:
        print("Opção inválida.")
    #aqui ele faz o fatorial do primeiro numero (num1)
        elif opcao == "7":
    if num1.is_integer() and num1 >= 0:
        resultado = math.factorial(int(num1))
        print(f"Fatorial de {int(num1)}:", resultado)
    else:
        print("Erro: O número deve ser um inteiro positivo para calcular o fatorial.")
    # aqui ele faz o seno do primeiro numero (num1)
    elif opcao == "8":
        resultado = math.sin(math.radians(num1))  # Converte de graus para radianos
        print(f"Seno de {num1} graus:", resultado)
    # aqui ele faz o cosseno do primeiro numero (num1)
    elif opcao == "9":
        resultado = math.cos(math.radians(num1))  # Converte de graus para radianos
        print(f"Cosseno de {num1} graus:", resultado)
    # aqui ele faz a tangente do primeiro numero (num1)
    elif opcao == "10":
        resultado = math.tan(math.radians(num1))  # Converte de graus para radianos
        print(f"Tangente de {num1} graus:", resultado)
    # aqui ele faz a porcentagem do primeiro numero (num1) em relação ao segundo numero (num2)
    elif opcao == "11":
        try:
            num2 = float(input("Digite o número para calcular a porcentagem de: "))
            resultado = (num1 / 100) * num2
            print(f"{num1}% de {num2} é:", resultado)
        except ValueError:
            print("Por favor, digite um número válido para o cálculo da porcentagem.")
    # aqui ele converte o primeiro numero (num1) de graus para radianos
    elif opcao == "12":
        resultado = math.radians(num1)
        print(f"{num1} graus em radianos é:", resultado)
    # aqui ele converte o primeiro numero (num1) de radianos para graus
    elif opcao == "13":
        resultado = math.degrees(num1)
        print(f"{num1} radianos em graus é:", resultado)
    # aqui ele mostra o historico de operações
    elif opcao == "14":
        print("Histórico de cálculos:")  
        for h in historico:
            print(h)
    else:
        print("Opção inválida.")
        elif opcao == "15":
        historico.clear()   
        #aqui é pra apagar historico
    print("Histórico apagado.") 
    elif opcao == "16":
    resultado = (num1 + num2) / 2
    print(f"Média entre {num1} e {num2} é:", resultado) 
    # aqui nois mexe em media e talz
        historico.append(f"Operação: {opcao} - Resultado: {resultado}")    
    elif opcao == "17": 
        #aqui é pra comparação de numeros (tipo maior,menor ou igual)
    if num1 > num2:
        resultado = f"{num1} é maior que {num2}"
    elif num1 < num2:
        resultado = f"{num1} é menor que {num2}"
    else:
        resultado = "Os dois números são iguais"
    print(resultado)
elif opcao == "18":  
    #aqui é a calculadora da area do triangulo
    try:
        base = float(input("Digite a base do triângulo: "))
        altura = float(input("Digite a altura do triângulo: "))
        resultado = (base * altura) / 2
        print(f"Área do triângulo com base {base} e altura {altura} é:", resultado)
    except ValueError:
        print("Valores inválidos.")
elif opcao == "19":
    resultado = round(num1) # aqui é pra arredondar o numero
    print(f"{num1} arredondado é:", resultado)
elif opcao == "20":
    resultado = -num1   
    print(f"Inverso de sinal de {num1} é:", resultado) # aqui inverte uns sinais
elif opcao == "21":
    if num2 != 0 and num1 % num2 == 0:
        resultado = f"{num1} é múltiplo de {num2}"
    else:
        resultado = f"{num1} NÃO é múltiplo de {num2}"
    print(resultado) #aqui verifica se os numeros são multiplos
    #aqui fica a media ponderada 
elif opcao == "22":
    try:
        nota1 = float(input("Digite a primeira nota: "))  
        peso1 = float(input("Digite o peso da primeira nota: "))
        nota2 = float(input("Digite a segunda nota: "))
        peso2 = float(input("Digite o peso da segunda nota: "))
        resultado = (nota1 * peso1 + nota2 * peso2) / (peso1 + peso2)
        print("Média ponderada:", resultado)
    except ValueError:
        print("Valores inválidos.")
        # aqui faz a media de varios numeros
        elif opcao == "23":
    try:
        qtd = int(input("Quantos números deseja calcular a média? ")) 
        for i in range(qtd):
            numero = float(input(f"Digite o número {i+1}: "))
            soma += numero
        resultado = soma / qtd
        print("Média dos números:", resultado)
    except ValueError:
        print("Entrada inválida.")
        #aqui faz potencia com o expoente negativo
elif opcao == "24":
    resultado = num1 ** (-abs(num2))  
    print(f"{num1} elevado a -{abs(num2)} é:", resultado)
    # aqui é so para saber se o numero é impa ou par ( kkkkkk)
elif opcao == "25":
    if int(num1) % 2 == 0:  
        resultado = f"{int(num1)} é par"
    else:
        resultado = f"{int(num1)} é ímpar"
    print(resultado) 
    #verificar se o numero é prpimo
elif opcao == "26":
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
    print(resultado) 
    #botei a função para a calculadora converter valores de reais pra dolar
elif opcao == "27":
    try:
        valor_em_reais = float(input("Digite o valor em reais: R$ ")) 
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
