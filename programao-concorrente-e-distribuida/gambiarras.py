import threading
import time

count = 0

lock = threading.Lock()

def incrementar():
    global count
    lock.acquire()
    try:
        for i in range (5000):
            x = count
            time.sleep(0.0001)
            x += 1 
            count = x
    finally:
        lock.release()



lista_threads = []
for _ in range(50):
    t = threading.Thread(target=incrementar)
    lista_threads.append(t)
    t.start()

for t in lista_threads:
    t.join()


print(f"Contador: {count}")