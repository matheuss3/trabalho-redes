def imprimeEstoque(estoque):
  print('\n#ESTOQUE#')
  for dictItem in estoque:
    print(f'Item: ' + dictItem['item'])
    print(f'Quantidade em estoque: ' + str(dictItem['qtdEstoque']))
    print(f'Valor unitário: ' + str(dictItem['vlUnitario']))
    print('---------------------')
  print()

import random

def criaPedidoVenda(estoque):
  itensPedido = []

  for i in range(5):
    itemSelected = random.choice(estoque)

    itemExists = False
    for itemPedido in itensPedido:
      if itemPedido['item'] == itemSelected['item']:
        itemPedido['qtdForn'] += 1
        itemExists = True
        break
    
    if not itemExists:
      itemPedido = { 
        'item': itemSelected['item'], 
        'qtdForn': 1,
        'vlUnitario': itemSelected['vlUnitario'] * 0.5
      }
      itensPedido.append(itemPedido)
    
  return itensPedido


import json

# Codifica um objeto para o envio
def codificar(obj, encode='UTF-8'):
  return json.dumps(obj, ensure_ascii=False).encode(encode)

# Decodifica um objeto recebido
def decodificar(msg, encode='UTF-8'):
  return json.loads(msg.decode(encode))


