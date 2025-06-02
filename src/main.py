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
    if b == 0:
        return 'operacao invalida'
    return a / b
    
def potencia(a,b):
    resultado = a ** b
    return resultado

def raiz_quadrada(a,b):
    resultado = a ** (1/b)
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

def converter_graus_para_radianos(a):
    resultado = a * (math.pi / 180)
    return resultado
    
def converter_radianos_para_graus(a):
    resultado = a * (180 / math.pi)
    return resultado    
    
def media_entre_dois_numeros(a,b):
    resultado = (a + b) / 2
    return resultado    
    
def comparar_dois_numeros(a,b):
    if a > b:
        resultado = f'{a} é maior que {b}'
    elif a < b:
        resultado = f'{a} é menor que {b}'
    else:
        resultado = f'{a} é igual a {b}'
    return resultado
    
def area_do_triangulo(base, altura):
    resultado = (base * altura) / 2
    return resultado
    
def arredondar_numeros(a):
    resultado = round(a)
    return resultado
    
def inverter_sinal(a):
    resultado = -a
    return resultado
    
def verificar_multiplos(a,b):
    if a % b == 0:
        resultado = f'{a} é múltiplo de {b}'
    else:
        resultado = f'{a} não é múltiplo de {b}'
    return resultado
    
def media_ponderada(n1, n2, peso1, peso2):
    resultado = (n1 * peso1 + n2 * peso2) / (peso1 + peso2)
    return resultado
    
def media_de_varios_numeros(lista):
    if not lista:
        return 0
    resultado = sum(lista) / len(lista)
    return resultado
    
def potencia_com_expoente_negativo(a, b):
    if b < 0:
        resultado = 1 / (a ** abs(b))
    else:
        resultado = a ** b
    return resultado
    
def verificar_par_ou_impar(a):
    if a % 2 == 0:
        resultado = f'{a} é par'
    else:
        resultado = f'{a} é ímpar'
    return resultado
    
def verificar_numero_primo(a):
    if a < 2:
        return f'{a} não é primo'
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            return f'{a} não é primo'
    return f'{a} é primo'   
    
def converter_reais_para_dolares(valor, cotacao):
    resultado = valor / cotacao
    return resultado
    
is_running = True
historico = []
a = 0
b = 0      

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

    a = float(input("Digite o primeiro número: "))
    
    if escolha in ['1', '2', '3', '4', '5', '6', '10', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22']:
        b = float(input("Digite o segundo número: "))

    if escolha == '1':
        resultado = soma(a, b)
        historico.append(f'{a} + {b} = {resultado}')
    
    elif escolha == '2':
        resultado = subtracao(a, b)
        historico.append(f'{a} - {b} = {resultado}')
    
    elif escolha == '3':
        resultado = multiplicacao(a, b)
        historico.append(f'{a} * {b} = {resultado}')
    
    elif escolha == '4':
        resultado = divisao(a, b)
        historico.append(f'{a} / {b} = {resultado}')
    elif escolha == '5':
        resultado = potencia(a, b)
        historico.append(f'{a} ** {b} = {resultado}')
    elif escolha == '6':
        resultado = raiz_quadrada(a, b)
        historico.append(f'{a}√{b} = {resultado}')
    elif escolha == '7':
        resultado = seno(a)
        historico.append(f'sin({a}) = {resultado}')
    elif escolha == '8':
        resultado = cos(a)
        historico.append(f'cos({a}) = {resultado}')
    elif escolha == '9':
        resultado = tangente(a)
        historico.append(f'tan({a}) = {resultado}')
    elif escolha == '10':
        resultado = porcentagem(a, b)
        historico.append(f'{a} * {b}% = {resultado}')
    elif escolha == '11':
        resultado = converter_graus_para_radianos(a)
        historico.append(f'{a} graus = {resultado} radianos')
    elif escolha == '12':
        resultado = converter_radianos_para_graus(a)
        historico.append(f'{a} radianos = {resultado} graus')
    elif escolha == '13':
        resultado = media_entre_dois_numeros(a, b)
        historico.append(f'Média entre {a}  e {b} = {resultado}')
    elif escolha == '14':
        resultado = comparar_dois_numeros(a, b)
        historico.append(resultado)
    elif escolha == '15':
        base = a
        altura = b
        resultado = area_do_triangulo(base, altura)
        historico.append(f'Área do triângulo com base {base} e altura {altura} = {resultado}')
    elif escolha == '16':
        resultado = arredondar_numeros(a)
        historico.append(f'Arredondamento de {a} = {resultado}')
    elif escolha == '17':
        resultado = inverter_sinal(a)
        historico.append(f'Inversão de sinal de {a} = {resultado}')
    elif escolha == '18':
        resultado = verificar_multiplos(a, b)
        historico.append(resultado)
    elif escolha == '19':
        peso1 = float(input("Digite o peso do primeiro número: "))
        peso2 = float(input("Digite o peso do segundo número: "))
        resultado = media_ponderada(a, b, peso1, peso2)
        historico.append(f'Média ponderada de {a} e {b} com pesos {peso1} e {peso2} = {resultado}')
    elif escolha == '20':
        numeros = input("Digite os números separados por vírgula: ")
        lista_numeros = [float(num) for num in numeros.split(',')]
        resultado = media_de_varios_numeros(lista_numeros)
        historico.append(f'Média dos números {lista_numeros} = {resultado}')
    elif escolha == '21':
        resultado = potencia_com_expoente_negativo(a, b)
        historico.append(f'{a} ** {b} = {resultado}')
    elif escolha == '22':
        resultado = verificar_par_ou_impar(a)
        historico.append(resultado)
    elif escolha == '23':
        resultado = verificar_numero_primo(a)
        historico.append(resultado)
    elif escolha == '24':
        cotacao = float(input("Digite a cotação do dólar: "))
        resultado = converter_reais_para_dolares(a, cotacao)
        historico.append(f'{a} reais = {resultado} dólares (cotação: {cotacao})')
    else:
        print("Operação inválida. Tente novamente.")
        continue