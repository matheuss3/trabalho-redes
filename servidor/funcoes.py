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


def imprimeSolicitacaoClienteConsumidor(pedido):
  print('#PEDIDO DO CLIENTE CONSUMIDOR#')

  for item in pedido:
    print('Item: ' + item['item'])
    print('Quantidade solicitada: ' + str(item['qtdPedida']))
    print()

import random

def procuraItemEstoque(item, estoque):
  for itemEstoque in estoque:
    if itemEstoque['item'] == item:
      return itemEstoque


def atendeSolicitacaoConsumidor(pedido, estoque):
  for itemPedido in pedido:
    itemEstoque = procuraItemEstoque(itemPedido['item'], estoque)
    itemEstoque['qtdEstoque'] -= itemPedido['qtdPedida']

    if itemEstoque['qtdEstoque'] < 0:
      return None
  
  return { 'pedido': random.randint(1, 1000000), 'itens': pedido }


import json

# Codifica um objeto para o envio
def codificar(obj, encode='UTF-8'):
  return json.dumps(obj, ensure_ascii=False).encode(encode)

# Decodifica um objeto recebido
def decodificar(msg, encode='UTF-8'):
  return json.loads(msg.decode(encode))