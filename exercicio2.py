nome = input('digite seu nome: ')
idade = input('digite sua idade: ')
print(idade)  
if nome and idade:
   print(f'Seu nome é {nome}')
   print(f'Seu nome invertido é {nome[::-1]}')
 
   if ' ' in nome: 
    print('Seu nome contém espaços')
   else:
    print('Seu nome Não contém espaços')

    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]} letras')
    print(f'A ultima letra do seu nome é {nome[-1]} letras') 

else:
    
    print("Desculpe,você deixou o campo vazios.")



