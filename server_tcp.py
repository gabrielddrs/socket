from socket import *

#Definindo endereço do servidor e porta de conexão
servidor = '127.0.0.1'
porta = 43210

#Criando o objeto do Socket
obj_socket = socket(AF_INET, SOCK_STREAM)
#o primeiro arg é o tipo de identificação com o server usando o endereço
#o segundo arg é para trabalhar com o metódo TCP
obj_socket.bind((servidor, porta))
obj_socket.listen(2) #Quantidade máximas de clientes

print("Aguardando cliente...")

while True:
    con, cliente = obj_socket.accept()
    print(f"Conectado com: {cliente}")
    while True:
        msg_recebida = str(con.recv(1024))
        print(f"Recebemos: {msg_recebida}")
        msg_enviada = 'Olá cliente'
        con.send(msg_enviada)
        break

    con.close()
