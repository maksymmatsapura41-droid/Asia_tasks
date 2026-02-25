import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(100000):
        # lock.acquire() — можно так, но лучше через context manager
        with lock:
            counter += 1

threads = []
for i in range(5):
    t = threading.Thread(target=increment)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"Final result of counter: {counter}")

# Thread 1
# counter = 0
# new_counter = counter + 1
#   Thread 2
#   counter =0
#   new_counter = counter + 1
#   counter = new_counter
# counter = new_counter