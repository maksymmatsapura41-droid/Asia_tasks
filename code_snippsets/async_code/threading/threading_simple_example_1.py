import threading
import time

def download_data(filename):
    print(f"Download start {filename}...")
    time.sleep(2) # switch to the another threading when blocked operation (I/O) occur
    print(f"File {filename} downloaded!")


start = time.time()
thread1 = threading.Thread(target=download_data, args=("image.png",))
thread2 = threading.Thread(target=download_data, args=("video.mp4",))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

end = time.time()
print(end - start)
print("All tasks finished!")