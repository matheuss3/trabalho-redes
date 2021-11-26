"""
Disciplina de Redes de Computadores
Semestre: 2021/2
Trabalho = "Protocolo loja de produtos esportivos"

Autor   = "Matheus de Souza"
Matricula = 20191BSI0301
E-mail  = "matheussouzapoliveira@gmail.com"
"""
def imprimeEstoque(estoque):
  print('\n#ESTOQUE#')
  for dictItem in estoque:
    print(f'Item: ' + dictItem['item'])
    print(f'Quantidade em estoque: ' + str(dictItem['qtdEstoque']))
    print(f'Valor unitário: ' + str(dictItem['vlUnitario']))
    print('---------------------')
  print()

def imprimeSolicitacaoCompra(pedido):
  print('#PEDIDO FEITO A LOJA#')

  for item in pedido:
    print('Item: ' + item['item'])
    print('Quantidade solicitada: ' + str(item['qtdPedida']))
    print('---------------------')
  print()

import random

def criaPedidoConsumidor(estoque):
  itensPedido = []

  for i in range(5):
    itemSelected = random.choice(estoque)

    itemExists = False
    for itemPedido in itensPedido:
      if itemPedido['item'] == itemSelected['item']:
        itemPedido['qtdPedida'] += 1
        itemExists = True
        break
    
    if not itemExists:
      itemPedido = { 'item': itemSelected['item'], 'qtdPedida': 1 }
      itensPedido.append(itemPedido)
    
  return itensPedido


import json

# Codifica um objeto para o envio
def codificar(obj, encode='UTF-8'):
  return json.dumps(obj, ensure_ascii=False).encode(encode)

# Decodifica um objeto recebido
def decodificar(msg, encode='UTF-8'):
  return json.loads(msg.decode(encode))


