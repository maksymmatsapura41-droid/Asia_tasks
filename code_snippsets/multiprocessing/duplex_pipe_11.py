from multiprocessing import Process, Pipe

def worker(conn):
    msg = conn.recv()  # получает от главного процесса
    conn.send(f"Got: {msg}")

if __name__ == "__main__":
    parent_conn, child_conn = Pipe()
    p = Process(target=worker, args=(child_conn,))
    p.start()

    parent_conn.send("Ping")
    print(parent_conn.recv())  # Got: Ping

    p.join()
