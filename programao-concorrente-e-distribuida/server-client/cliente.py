import json
import socket

host = '127.0.0.1'
port = 8080

mensagem = {
    "id": 1234,
    "comando": "Consultar saldo",
    "conta": "45678-9"
}

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    s.sendall(json.dumps(mensagem).encode('utf-8'))
    print(f'Mensagem {json.dumps(mensagem).encode('utf-8')} enviada!')

    resposta = s.recv(1024)
    print(f"Resposta: {resposta.decode('utf-8')}")