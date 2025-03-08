import threading
import time

count = 0

L = threading.Lock() # Bloqueia o uso das varáveis já declaradas em diferentes threads simultâneas

def incrementar():
    global count
    for i in range (1000):
        L.acquire() # Ativa o bloqueio nesse ponto

        try:
            x = count
            time.sleep(0.0001)
            x += 1 
            count = x
        finally:
            L.release() # Desbloqueia nesse ponto
        
ta = threading.Thread(target= incrementar)
tb = threading.Thread(target= incrementar)
tc = threading.Thread(target= incrementar)

ta.start()
tb.start()
tc.start()

ta.join()
tb.join()
tc.join()

print(f"Contador: {count}")