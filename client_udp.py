#Importando o módulo
from socket import *

#Criando o servidor e endereçando
server = '127.0.0.1'
port = 43210

#Criando o objeto Socket
obj_socket = socket(AF_INET, SOCK_DGRAM)
obj_socket.connect((server, port))
saida=''

#Iteração para diálogo
while saida != "exit":
    msg = input("Cliente: ")
    obj_socket.sendto(msg.encode(), (server, port))
    dados, origem = obj_socket.recvfrom(65535)
    print(f"Servidor: {dados.decode()}")
    saida = input("Caso deseje sair, digite <exit>: ").lower()

#Fechamento do objeto
obj_socket.close()
