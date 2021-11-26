"""
Disciplina de Redes de Computadores
Semestre: 2021/2
Trabalho = "Aprendendo redes"

Autor   = "Matheus de Souza"
E-mail  = "matheussouzapoliveira@gmail.com"
"""

import os

os.chdir(os.path.dirname(os.path.realpath(__file__)))

from socket import *

from funcoes import *

HOST = 'localhost'
PORT = 5000
BYTES_BY_MSG = 5000
CODING = 'UTF-8'

tcp = socket(AF_INET, SOCK_STREAM)

tcp.bind((HOST, PORT))
tcp.listen(10)

print('Servidor iniciado!')
print(f'Host: {HOST}\tPort: {PORT}')


while True:
  con, cliente = tcp.accept()
  print('\nCliente', cliente) # Imprime os dados do cliente conectado
  
  clienteConsumidorFornecedor = con.recv(BYTES_BY_MSG).decode(CODING).upper() # Salva mensagem que diz se o cliente é um consumidor ou um fornecedor
  print('Cliente', clienteConsumidorFornecedor, '\n') # Imprime Resposta - CONSUMIDOR || FORNECEDOR

  estoque = leEstoque() # Retorna um objeto com os itens e a quantidade em estoque
  objSend = codificar(estoque) # Codifica o estoque
  con.send(objSend) # Envia o objeto codificado

  if (clienteConsumidorFornecedor == 'CONSUMIDOR'):
    respostaCliente = con.recv(BYTES_BY_MSG) # Resposta com solicitação de compras
    solicitacaoCliente = decodificar(respostaCliente) # decodifica mensagem recebida
    imprimeSolicitacaoClienteConsumidor(solicitacaoCliente)

    pedido = atendeSolicitacaoConsumidor(solicitacaoCliente, estoque) # Verifica se o pedido pode ser atendido ou não, retorna None se falta estoque

    if not pedido: # Pedido não pode ser atendido
      con.send(codificar({ 'message': 'O pedido nao foi concluido por falta de estoque' }))
    else:
      con.send(codificar(pedido))
      print('Pedido realizado com sucesso! :D\n')
      imprimeEstoque(estoque)
  else:
    respostaCliente = con.recv(BYTES_BY_MSG) # Resposta com solicitação de vendas para a loja
    solicitacaoCliente = decodificar(respostaCliente) # decodifica mensagem recebida
    imprimeSolicitacaoClienteFornecedor(solicitacaoCliente)

    resposta = input('Deseja realizar essa compra? (s/n)') # Verificação se a loja quer fazer a compra
    print(resposta.upper())
    if (resposta.upper() == 'S'): # Pedido aceito
      realizaCompra(solicitacaoCliente, estoque)
      print('Compra da loja!')
      con.send(codificar({ 'message': 'A compra foi aceita pela loja! :D' }))
      imprimeEstoque(estoque)
    else:
      print('Pedido rejeitado')
      con.send(codificar({ 'message': 'Pedido rejeitado! :(' }))
  con.close()
  