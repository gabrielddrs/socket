#Importando o módulo
from socket import *

#Criando o server
server = '127.0.0.1'
port = 43210

#Criando o objeto Socket
obj_socket = socket(AF_INET, SOCK_DGRAM)
obj_socket.bind((server, port))
print("Servidor conectado...")

#Iteração para diálogo
while True:
    dados, origem = obj_socket.recv(65535)
    print(f"Origem.....: {origem}")
    print(f"Dados recebidos...: {dados}")
    resposta = input("Servidor: ")
    obj_socket.sendto(resposta.encode(), origem)

obj_socket.close()
