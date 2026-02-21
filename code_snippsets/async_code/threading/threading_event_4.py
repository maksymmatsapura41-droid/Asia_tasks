import threading
import time

start_signal = threading.Event()

def racer(name):
    print(f"Driver {name} on start...")
    start_signal.wait() # Ждет, пока флаг станет True
    print(f"Driver {name} Go!")

for i in range(3):
    threading.Thread(target=racer, args=(i,)).start()

time.sleep(2)
print("Go!")
start_signal.set() # Устанавливает флаг в True, все wait() срабатывают