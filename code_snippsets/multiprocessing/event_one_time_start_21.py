import multiprocessing
import time


def racer(event, name):
    print(f"Racer {name} is at the starting line...")
    event.wait()
    print(f"--- RACER {name} STARTED! ---")


if __name__ == "__main__":
    start_signal = multiprocessing.Event()

    racers = [
        multiprocessing.Process(target=racer, args=(start_signal, i))
        for i in range(3)
    ]

    for r in racers:
        r.start()

    print("Preparing for the start (3 seconds)...")
    time.sleep(3)

    print("GO!")
    start_signal.set()

    for r in racers:
        r.join()
