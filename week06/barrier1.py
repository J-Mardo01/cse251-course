import threading
import time


def test_with_barrier(synchronizer: threading.Barrier):

    synchronizer.wait()
    now = time.time()

    print(f'{threading.current_thread().name}, {now=}\n', end="")

if __name__ == '__main__':
    
    synchronizer = threading.Barrier(2)

    t1 = threading.Thread(target = test_with_barrier, args =(synchronizer,))
    t2 = threading.Thread(target = test_with_barrier, args =(synchronizer,))

    t1.start()
    t2.start()
    t1.join()
    t2.join()