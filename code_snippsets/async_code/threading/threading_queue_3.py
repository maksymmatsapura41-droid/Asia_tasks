import threading
import queue
import time

q = queue.Queue()

def worker():
    while True:
        item = q.get()
        if item is None: break
        print(f"Tash processing: {item}")
        time.sleep(1)
        q.task_done()

threads = []
for i in range(2):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

time.sleep(2)

for item in ["Load photo", "Send email", "Refresh database"]:
    q.put(item)


q.join()

# look on loop of queues

for i in range(len(threads)): q.put(None)