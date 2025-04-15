import socket
import threading

HOST = 'localhost'
PORT = 12345
NUM_ASSENTOS = 100

assentos = [False] * NUM_ASSENTOS  # False = livre, True = reservado
lock = threading.Lock()

def tratar_cliente(conn, addr):
    print(f"[CONECTADO] Cliente {addr} conectado.")
    try:
        while True:
            dados = conn.recv(1024).decode()
            if not dados:
                break

            pedidos = list(map(int, dados.strip().split(',')))
            print(f"[REQUISIÇÃO] Cliente {addr} solicitou: {pedidos}")

            with lock:
                sucesso = []
                falha = []
                for assento in pedidos:
                    if 1 <= assento <= NUM_ASSENTOS:
                        if not assentos[assento - 1]:
                            assentos[assento - 1] = True
                            sucesso.append(assento)
                        else:
                            falha.append(assento)
                    else:
                        falha.append(assento)

            resposta = f"Reservados: {sucesso} | Indisponíveis/Inválidos: {falha}"
            print(f"[RESPOSTA] Para {addr}: {resposta}")
            conn.send(resposta.encode())

    except Exception as e:
        print(f"[ERRO] Cliente {addr} - {e}")
    finally:
        conn.close()
        print(f"[DESCONECTADO] Cliente {addr} desconectado.")

def iniciar_servidor():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"[SERVIDOR] Aguardando conexões em {HOST}:{PORT}...")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=tratar_cliente, args=(conn, addr))
        thread.start()
        print(f"[ATIVO] Conexões ativas: {threading.active_count() - 1}")

if __name__ == "__main__":
    iniciar_servidor()
