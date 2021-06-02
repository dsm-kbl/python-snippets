from queue_code import Queue
from threading import Thread, Lock, currentThread


def worker(q, lock):
    while True:
        value = q.get()

        # processing ...
        with lock:
            print(f'in {currentThread().name} got {value}')
        q.task_done()


if __name__ == "__main__":
    q = Queue()
    lock = Lock()

    num_of_threads = 10

    for i in range(num_of_threads):
        thread = Thread(target=worker, args=(q, lock))
        thread.daemon = True
        thread.start()

    for i in range(1, 21):
        q.put(i)

    q.join()

    print('end main')


