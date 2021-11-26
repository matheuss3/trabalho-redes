import os

def leEstoque():
  estoque = []

  arquivoEstoque = open('database/estoque.csv')

  arquivoEstoque.readline() # Pulando cabeçalho

  linha = arquivoEstoque.readline()
  while linha != '':
    item, qtdEstoque, vlUnitario = linha.strip().split(';')

    dictItem = {
      'item': item,
      'qtdEstoque': int(qtdEstoque),
      'vlUnitario': float(vlUnitario)
    }

    estoque.append(dictItem)

    linha = arquivoEstoque.readline()
  
  return estoque

def imprimeEstoque(estoque):
  print('\n#ESTOQUE#')
  for dictItem in estoque:
    print(f'Item: ' + dictItem['item'])
    print(f'Quantidade em estoque: ' + str(dictItem['qtdEstoque']))
    print(f'Valor unitário: ' + str(dictItem['vlUnitario']))
    print('---------------------')
  print()

def imprimeSolicitacaoClienteConsumidor(pedido):
  print('#PEDIDO DO CLIENTE CONSUMIDOR#')

  for item in pedido:
    print('Item: ' + item['item'])
    print('Quantidade solicitada: ' + str(item['qtdPedida']))
    print('---------------------')
  print()

def imprimeSolicitacaoClienteFornecedor(pedido):
  print('#PEDIDO DO CLIENTE FORNECEDOR#')

  for item in pedido:
    print('Item: ' + item['item'])
    print('Quantidade fornecida: ' + str(item['qtdForn']))
    print('Valor unitario: ' + str(item['vlUnitario']))
    print('---------------------')
  print()


import random

def procuraItemEstoque(item, estoque):
  for itemEstoque in estoque:
    if itemEstoque['item'] == item:
      return itemEstoque


def atendeSolicitacaoConsumidor(solicitacao, estoque):
  pedido = { 'numero_pedido': random.randint(1, 1000000), 'vlTotal': 0, 'itens': [] }

  for itemSolicitado in solicitacao:
    itemEstoque = procuraItemEstoque(itemSolicitado['item'], estoque)
    itemEstoque['qtdEstoque'] -= itemSolicitado['qtdPedida']

    if itemEstoque['qtdEstoque'] < 0:
      return None
    
    pedido['itens'].append({
      'item': itemSolicitado['item'],
      'quantidade': itemSolicitado['qtdPedida'],
      'valorUnitario': itemEstoque['vlUnitario']
    })

    pedido['vlTotal'] += itemEstoque['vlUnitario'] * itemSolicitado['qtdPedida']

  atualizaEstoque(estoque)
  return pedido

def realizaCompra(solicitacao, estoque):
  for itemSolicitado in solicitacao:
    itemEstoque = procuraItemEstoque(itemSolicitado['item'], estoque)
    itemEstoque['qtdEstoque'] += itemSolicitado['qtdForn']

  atualizaEstoque(estoque)

def atualizaEstoque(estoque):
  fileEstoque = open('database/estoque.csv', 'w')

  fileEstoque.write('item;estoque;vl_unitario\n')

  for itemEstoque in estoque:
    item = itemEstoque['item']
    qtdEstoque = itemEstoque['qtdEstoque']
    vlUnitario = itemEstoque['vlUnitario']

    fileEstoque.write(f'{item};{qtdEstoque};{vlUnitario}\n')

import json

# Codifica um objeto para o envio
def codificar(obj, encode='UTF-8'):
  return json.dumps(obj, ensure_ascii=False).encode(encode)

# Decodifica um objeto recebido
def decodificar(msg, encode='UTF-8'):
  return json.loads(msg.decode(encode))