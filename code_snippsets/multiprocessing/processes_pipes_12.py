from multiprocessing import Process, Pipe
import time

def worker1(conn):
    conn.send("Hello from worker1")
    msg = conn.recv()
    print(f"Worker1 received: {msg}")
    conn.close()

def worker2(conn):
    msg = conn.recv()
    print(f"Worker2 received: {msg}")
    conn.send("Hello from worker2")
    conn.close()

if __name__ == "__main__":
    conn1, conn2 = Pipe()

    p1 = Process(target=worker1, args=(conn1,))
    p2 = Process(target=worker2, args=(conn2,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
