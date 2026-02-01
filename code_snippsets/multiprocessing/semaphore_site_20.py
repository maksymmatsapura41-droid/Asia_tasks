import multiprocessing

import requests
import time


def prepare_data():
    print("Preparing data...")

def process_response(response):
    print(f"Processing data... {response}")


def fetch_url(sem, url):
    prepare_data()

    with sem:
        response = requests.get(url)
        print(f"Downloaded: {url}")
        time.sleep(1)  # Small delay to avoid sending requests too frequently

    # Further heavy processing (again, without any limits)
    process_response(response)


if __name__ == "__main__":
    sem = multiprocessing.Semaphore(4)
    url = "https://www.google.com"

    processes = [multiprocessing.Process(target=fetch_url, args=(sem, url)) for _ in range(8)]

    for process in processes:
        process.start()

    for process in processes:
        process.join()