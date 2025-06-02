def soma(a,b):
    resultado = a + b
    return resultado

def subtracao(a,b):
    resultado = a - b
    return resultado

def multiplicacao(a,b):
    resultado = a * b
    return resultado    

def divisao(a,b):
    if n2 == 0:
        resultado = 'operação inválida'
    return resultado
    else:
        resultado = a / b
        historico.append(f'{n1} / {n2} = {resultado}')
    return resultado
    
def potencia(a,b):
    resultado = a ** b
    return resultado

def raiz_quadrada(a,b):
    resultado = a ** (1/b)
    historico.append(f1{n2}√{n1} = {resultado}')
    return resultado
    
def seno (a):
    resultado = math.sin(a)
    return resultado    
    
def cos (a):
    resultado = math.cos(a)
    return resultado
    
def tangente(a):
    resultado = math.tan(a)
    return resultado
    
def porcentagem(a,b):
    resultado = (a * b) / 100
    return resultado

def converter graus para radianos(a):
    resultado = a * (math.pi / 180)
    return resultado
    
def converter radianos para graus(a):
    resultado = a * (180 / math.pi)
    return resultado    
    
def média entre dois números(a,b):
    resultado = (a + b) / 2
    return resultado    
    
def comparar dois números(a,b):
    if a > b:
        resultado = f'{a} é maior que {b}'
    elif a < b:
        resultado = f'{a} é menor que {b}'
    else:
        resultado = f'{a} é igual a {b}'
    return resultado
    
def area do triangulo(base, altura):
    resultado = (base * altura) / 2
    return resultado
    
def arredondar numeros(a):
    resultado = round(a)
    return resultado
    
def inverter sinal(a):
    resultado = -a
    return resultado
    
def verificar múltiplos(a,b):
    if a % b == 0:
        resultado = f'{a} é múltiplo de {b}'
    else:
        resultado = f'{a} não é múltiplo de {b}'
    return resultado
    
def media ponderada(n1, n2, peso1, peso2):
    resultado = (n1 * peso1 + n2 * peso2) / (peso1 + peso2)
    return resultado
    
def media de varios numeros(lista):
    if not lista:
        return 0
    resultado = sum(lista) / len(lista)
    return resultado
    
def potencia com expoente negativo(a, b):
    if b < 0:
        resultado = 1 / (a ** abs(b))
    else:
        resultado = a ** b
    return resultado
    
def verificar par ou ímpar(a):
    if a % 2 == 0:
        resultado = f'{a} é par'
    else:
        resultado = f'{a} é ímpar'
    return resultado
    
def verificar numero primo(a):
    if a < 2:
        return f'{a} não é primo'
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            return f'{a} não é primo'
    return f'{a} é primo'   
    
def converter reais para dolares(valor, cotacao):
    resultado = valor / cotacao
    return resultado
    
is_running = True
historico = []
n1 = 0
n2 = 0      

while is_running == True:
    print('Selecione uma operação:')
    print('1. Soma')
    print('2. Subtração')
    print('3. Multiplicação')
    print('4. Divisão')
    print('5. Potência')
    print('6. Raiz Quadrada')
    print('7. Seno')
    print('8. Cosseno')
    print('9. Tangente')
    print('10. Porcentagem')
    print('11. Converter graus para radianos')
    print('12. Converter radianos para graus')
    print('13. Média entre dois números')
    print('14. Comparar dois números')
    print('15. Área do triângulo')
    print('16. Arredondar números')
    print('17. Inverter sinal')
    print('18. Verificar múltiplos')
    print('19. Média ponderada')
    print('20. Média de vários números')
    print('21. Potência com expoente negativo')
    print('22. Verificar par ou ímpar')
    print('23. Verificar número primo')
    print('24. Converter reais para dólares')
    print('25. Sair')

    escolha = input("Digite o número da operação: ")

    if escolha == '25':
        is_running = False
        continue

    n1 = float(input("Digite o primeiro número: "))
    
    if escolha in ['1', '2', '3', '4', '5', '6', '10', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22']:
        n2 = float(input("Digite o segundo número: "))

    if escolha == '1':
        resultado = soma(n1, n2)
        historico.append(f'{n1} + {n2} = {resultado}')
    
    elif escolha == '2':
        resultado = subtracao(n1, n2)
        historico.append(f'{n1} - {n2} = {resultado}')
    
    elif escolha == '3':
        resultado = multiplicacao(n1, n2)
        historico.append(f'{n1} * {n2} = {resultado}')
    
    elif escolha == '4':
        resultado = divisao(n1, n2)
        historico.append(f'{n1} / {n2} = {resultado}')
    elif escolha == '5':
        resultado = potencia(n1, n2)
        historico.append(f'{n1} ** {n2} = {resultado}')
    elif escolha == '6':
        resultado = raiz_quadrada(n1, n2)
        historico.append(f'{n2}√{n1} = {resultado}')
    elif escolha == '7':
        resultado = seno(n1)
        historico.append(f'sin({n1}) = {resultado}')
    elif escolha == '8':
        resultado = cos(n1)
        historico.append(f'cos({n1}) = {resultado}')
    elif escolha == '9':
        resultado = tangente(n1)
        historico.append(f'tan({n1}) = {resultado}')
    elif escolha == '10':
        resultado = porcentagem(n1, n2)
        historico.append(f'{n1} * {n2}% = {resultado}')
    elif escolha == '11':
        resultado = converter_graus_para_radianos(n1)
        historico.append(f'{n1} graus = {resultado} radianos')
    elif escolha == '12':
        resultado = converter_radianos_para_graus(n1)
        historico.append(f'{n1} radianos = {resultado} graus')
    elif escolha == '13':
        resultado = média_entre_dois_números(n1, n2)
        historico.append(f'Média entre {n1} e {n2} = {resultado}')
    elif escolha == '14':
        resultado = comparar_dois_números(n1, n2)
        historico.append(resultado)
    elif escolha == '15':
        base = n1
        altura = n2
        resultado = area_do_triangulo(base, altura)
        historico.append(f'Área do triângulo com base {base} e altura {altura} = {resultado}')
    elif escolha == '16':
        resultado = arredondar_numeros(n1)
        historico.append(f'Arredondamento de {n1} = {resultado}')
    elif escolha == '17':
        resultado = inverter_sinal(n1)
        historico.append(f'Inversão de sinal de {n1} = {resultado}')
    elif escolha == '18':
        resultado = verificar_multiplos(n1, n2)
        historico.append(resultado)
    elif escolha == '19':
        peso1 = float(input("Digite o peso do primeiro número: "))
        peso2 = float(input("Digite o peso do segundo número: "))
        resultado = media_ponderada(n1, n2, peso1, peso2)
        historico.append(f'Média ponderada de {n1} e {n2} com pesos {peso1} e {peso2} = {resultado}')
    elif escolha == '20':
        numeros = input("Digite os números separados por vírgula: ")
        lista_numeros = [float(num) for num in numeros.split(',')]
        resultado = media_de_varios_numeros(lista_numeros)
        historico.append(f'Média dos números {lista_numeros} = {resultado}')
    elif escolha == '21':
        resultado = potencia_com_expoente_negativo(n1, n2)
        historico.append(f'{n1} ** {n2} = {resultado}')
    elif escolha == '22':
        resultado = verificar_par_ou_impar(n1)
        historico.append(resultado)
    elif escolha == '23':
        resultado = verificar_numero_primo(n1)
        historico.append(resultado)
    elif escolha == '24':
        cotacao = float(input("Digite a cotação do dólar: "))
        resultado = converter_reais_para_dolares(n1, cotacao)
        historico.append(f'{n1} reais = {resultado} dólares (cotação: {cotacao})')
    else:
        print("Operação inválida. Tente novamente.")
        continue