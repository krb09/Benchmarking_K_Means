import datetime as dt
from multiprocessing import Process, current_process
import sys
import time

def f(name):
    print('{}: hello {} from {}'.format(
        time.time(), name, current_process().name))
    sys.stdout.flush()

if __name__ == '__main__':
    worker_count = 44
    worker_pool = []
    for _ in range(worker_count):
        p = Process(target=f, args=('Kartik',))
        p.start()
        worker_pool.append(p)
    for p in worker_pool:
        p.join()  # Wait for all of the workers to finish.

    # Allow time to view results before program terminates.
    a = raw_input("Finished")  # input(...) in Python 3
