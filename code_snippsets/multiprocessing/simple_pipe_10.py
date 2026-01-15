from multiprocessing import Process, Pipe

def worker(conn):
    conn.send("Hello from worker")
    conn.close()

if __name__ == "__main__":
    parent_conn, child_conn = Pipe()
    p = Process(target=worker, args=(child_conn,))
    p.start()

    msg = parent_conn.recv()  # ждет, пока worker отправит данные
    print(msg)  # Hello from worker

    p.join()
