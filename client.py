import socket


# TCP protocol
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = 'localhost'
PORT = 50000

client.connect((HOST, PORT))
print('Conectado\n')



message = (input('Digite sua mensagem: '))
data = bytearray('\2' + message + '\3', 'utf-8')


checksum = 0

for element in message.encode():
    checksum ^= element


data.append(checksum)

client.sendall(data)

data_client_received = client.recv(1024)
print(f'\nA Mensagem entregue: ({data_client_received.decode()})')
