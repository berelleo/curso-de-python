"""
Repetições
enquanto (enquanto)
Executar uma ação enquanto uma condição para verdadeira
Loop infinito -> Quando um código não tem fim
"""
contador  =  0

while  contador  <=  100:
    contador  +=  1

    if  contador  ==  6 :
        print ( 'Não vou mostrar o 6.' )
        continue

    if  contador  >=  10  and  contador  <=  27 :
        print ( 'Não vou mostrar o' , contador )
        continue

    input( contador )

    if contador  ==  40 :
        break


print( 'Acabou' )

