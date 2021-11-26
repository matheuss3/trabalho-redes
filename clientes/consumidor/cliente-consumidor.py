"""
Disciplina de Redes de Computadores
Semestre: 2021/2
Trabalho = "Protocolo loja de produtos esportivos"

Autor   = "Matheus de Souza"
Matricula = 20191BSI0301
E-mail  = "matheussouzapoliveira@gmail.com"
"""
from socket import *
from funcoes import *

import json

HOST = 'localhost'
PORT = 5000
BYTES_BY_MSG = 5000
CODING = 'UTF-8'

tcp = socket(AF_INET, SOCK_STREAM)
tcp.connect((HOST, PORT))

tcp.send('consumidor'.encode(CODING))

respostaServidor = tcp.recv(BYTES_BY_MSG)

estoque = decodificar(respostaServidor)
imprimeEstoque(estoque)

pedidoConsumidor = criaPedidoConsumidor(estoque) # Cria um pedido aleatório com base nos itens em estoque
imprimeSolicitacaoCompra(pedidoConsumidor)
tcp.send(codificar(pedidoConsumidor))

respostaServidor = tcp.recv(BYTES_BY_MSG)

pedido = decodificar(respostaServidor)
print(json.dumps(pedido, indent=2))

tcp.close()