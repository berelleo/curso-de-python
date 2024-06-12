entrada = input('digite o horário ')
try:
    horas = int(entrada)
    if horas >= 0 and horas <= 11:
          print('Bom dia')
    elif horas >= 12 and horas <= 17  :
         print('boa tarde ')
    elif horas >= 17 and horas <= 23 :
      
       
         print('boa noite')
    else :
       print('Digite a hora Certa!! ' ) 

except:
  print( 'Erro!!!, digite um numero inteiro')