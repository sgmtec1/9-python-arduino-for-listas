# FOR / LISTA
from pyfirmata import Arduino
import lcd
import time

board=Arduino ('COM6')

compras = ['ARROZ         ', 'FEIJAO           ', 'CARNE         ', 'PAO          ']
for i in compras:
    lcd.escrever(board, 0, 0, 'LISTA DE COMPRAS       ')
    lcd.escrever(board, 0, 1, f'{i}')
    print(i)
    time.sleep(3.0)

for x in range(0,6):
    lcd.escrever(board, 0, 0, 'QTDE DE ITENS          ')
    lcd.escrever(board, 0, 1, f'NUMERO {x}                   ')
    print('QUANTIDADE')
    print(f'NUMERO  {x}            ')
    time.sleep(1.0)

nomes = ['PEDRO', 255, 'LETICIA']
for n in nomes:
    lcd.escrever(board, 0, 0, 'LISTA DE PESSOAS       ')
    lcd.escrever(board, 0, 1, f'{n}                   ')
    print('LISTA DE PESSOAS')
    print(n)
    time.sleep(2.0)

nomes = ['PEDRO           ', 'JOAO           ', 'LETICIA          ']

for laco in nomes:
    print(laco)
    lcd.escrever(board, 0, 0, 'LISTA DE PESSOAS')
    lcd.escrever(board, 0, 1, f'{laco}                ')
    print(laco)
    time.sleep(2.0)
else:
    print('----Fim da lista!!! ----')
    lcd.escrever(board, 0, 0, 'SGMTEC1                ')
    lcd.escrever(board, 0, 1, 'FIM DA LISTA           ')
    time.sleep(5.0)

time.sleep(100.0)
lcd.limpar(board)
board.exit()