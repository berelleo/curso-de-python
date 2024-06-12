import random
import sys

seis_digitos =''
for i in range(5):
    seis_digitos += str(random.randint(0,60))

print(seis_digitos)
sys.exit()
