import multiprocessing
import time


def db_worker(sem, process_num):
    print(f"Process {process_num} is trying to connect to the database...")

    with sem:
        print(f"  [OK] Process {process_num} acquired a slot. Working...")
        time.sleep(2)
        print(f"  [DONE] Process {process_num} finished work and released the slot.")



if __name__ == "__main__":
    connection_limit = multiprocessing.Semaphore(5)

    processes = []
    for i in range(7):
        p = multiprocessing.Process(
            target=db_worker,
            args=(connection_limit, i)
        )
        processes.append(p)
        p.start()

    for p in processes:
        p.join()
