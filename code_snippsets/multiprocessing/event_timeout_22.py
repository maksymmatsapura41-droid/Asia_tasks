import multiprocessing
import time
import logging


def data_loader(event, name):
    print(f"[{name}] Checking system readiness...")
    is_ready = event.wait(timeout=5)

    if is_ready:
        print(f"[{name}] System is ready! Starting data loading...")
    else:
        print(
            f"[{name}] ERROR: Wait timeout exceeded. "
            "The API did not respond in time. Shutting down."
        )


def initializer(event, should_fail=False):
    if should_fail:
        print("[Init] Simulating failure: the signal will never be sent...")
        time.sleep(10)  # Simulate long-running / stuck initialization
    else:
        print("[Init] Setting up the connection...")
        time.sleep(2)
        print("[Init] Connection established!")
        event.set()


if __name__ == "__main__":
    ready_event = multiprocessing.Event()

    fail_scenario = True

    loader = multiprocessing.Process(
        target=data_loader,
        args=(ready_event, "Loader-1")
    )
    init = multiprocessing.Process(
        target=initializer,
        args=(ready_event, fail_scenario)
    )

    loader.start()
    init.start()

    loader.join()
    init.join()
