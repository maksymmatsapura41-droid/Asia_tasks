import asyncio
import time


def download_file_sync(name):
    print("[Download] Downloading file...")
    time.sleep(1)
    print(f"[Download] Downloaded file {name}")


def main():
    start = time.time()
    download_file_sync("download_file_sync")
    download_file_sync("download_file_sync2")
    download_file_sync("download_file_sync3")
    end = time.time()
    print(str(end-start))


if __name__ == "__main__":
    main()