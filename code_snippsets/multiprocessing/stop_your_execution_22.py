import multiprocessing
import time


def monitor_service(stop_event):
    print("Monitoring service started...")
    while not stop_event.is_set():
        print("Checking system resources...")
        time.sleep(1)

    print("Stop signal received. Saving logs and shutting down...")


if __name__ == "__main__":
    stop_flag = multiprocessing.Event()

    service = multiprocessing.Process(
        target=monitor_service,
        args=(stop_flag,)
    )
    service.start()

    time.sleep(5)

    print("Main process: time to stop the service.")
    stop_flag.set()

    service.join()
    print("System has been fully shut down.")
