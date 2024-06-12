def multiplicador(numero):
    a = 3 # esta variavel tem o escopo local
    print(f'Dentro da função, a variavel a vale: {a}')
    return a * numero

a = 3 # esta variavel  tem o escopo global
b = multiplicador(6)
print(f'Fora da função, a variavel a vale : {b}')


