from socket import *
from funcoes import *

import json

HOST = 'localhost'
PORT = 5000
BYTES_BY_MSG = 5000
CODING = 'UTF-8'

tcp = socket(AF_INET, SOCK_STREAM)
tcp.connect((HOST, PORT))

tcp.send('fornecedor'.encode(CODING))

respostaServidor = tcp.recv(BYTES_BY_MSG)

estoque = decodificar(respostaServidor)
imprimeEstoque(estoque)

pedidoVendaLoja = criaPedidoVenda(estoque) # Cria um pedido aleatório com base nos itens em estoque
print(json.dumps(pedidoVendaLoja, indent=2))

tcp.send(codificar(pedidoVendaLoja))

respostaServidor = tcp.recv(BYTES_BY_MSG)

resposta = decodificar(respostaServidor)
print(json.dumps(resposta, indent=2))

tcp.close()