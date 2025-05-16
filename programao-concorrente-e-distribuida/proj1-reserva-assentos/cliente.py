import socket

HOST = 'localhost'
PORT = 12345

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print("✅ Conectado ao servidor.")

        while True:
            entrada = input("Digite os assentos para reservar (ex: 5,10,22) ou 'sair': ")
            if entrada.lower() == 'sair':
                break

            s.send(entrada.encode())
            resposta = s.recv(1024).decode()
            print(f"[RESPOSTA] {resposta}")

if __name__ == "__main__":
    main()
