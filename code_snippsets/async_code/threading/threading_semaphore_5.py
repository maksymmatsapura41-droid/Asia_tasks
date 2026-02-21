import threading
import time

# Разрешаем только 2 потока одновременно
pool = threading.Semaphore(2)

def access_resource(id):
    with pool:
        print(f"Thread {id} get access")
        time.sleep(2)
        print(f"Thread {id} free space")

for i in range(5):
    threading.Thread(target=access_resource, args=(i,)).start()