import queue
import multiprocessing

def write_function(q: queue.Queue):
    for i in range(10):
        q.put(i)

def read_function(q: queue.Queue):
    for _ in range(10):
        print(f"queue item = {q.get()}")




if __name__ == '__main__':
    
    #q = queue.Queue()

    q = multiprocessing.Queue()

    data = multiprocessing.Manager().list([0] * 3)

    p1 = multiprocessing.Process(target = read_function, args=(q,))
    p2 = multiprocessing.Process(target = write_function, args=(q,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()