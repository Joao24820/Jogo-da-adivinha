from time import sleep

from random import randint

Pc = randint(0, 10)
print('-=-' * 20)
print('vou pensar em um numero de 0 a 10. tente adivinhar...')
print('-=-' * 20)
print('Carregando...')
sleep(1)
print('Carregando...')
sleep(1)
print('Carregando...')
sleep(1)
jg = int(input('Em que numero eu pensei entre 0 e 10 ?\nResposta:'))
while jg <= 10:
    if jg == Pc:
        print('PARABENS !! VOCE CONSEGUIU ME VENCER !!')
    else:
        print('ERRADO !!, EU PENSEI NO NUMERO {} E NÃO NO NUMERO {}'.format(Pc, jg))
        break
else:
    print('Opção invalida')
