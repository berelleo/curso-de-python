# Calculadora
while True:
    numero_1 =  input('Digite o número:')
    numero_2 =  input('Digite outro número:')
    operador =  input('Digite o operador(+-/*):')

    numeros_validos = None
    nun_1_float = 0
    nun_2_float = 0

    try:
        nun_1_float = float(numero_1)
        nun_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None
    
    if numeros_validos is None:
        print('Um ou ambos os numero digitados são invalidos.')
        continue

    operadores_validos = '+-/*'
    if operador not in operadores_validos:
        print('operador inválido.')
    continue    
    if len(operador) > 1:
        print('Digite apenas um operador.')
    continue    
    
    if operador == '+':
        print(nun_1_float + nun_2_float)


    elif operador == '-': 
        print(nun_1_float - nun_2_float)
        
    elif operador == '*':
        print(nun_1_float * nun_2_float)

    elif operador == '/':
        print(nun_1_float / nun_2_float)

    else:      
        print('nunca deveria chegar aqui. ') 



    sair = input('Quer sair?[s]im: ').lower().startswith('s')

    if sair is True:
        break