from multiprocessing import Queue, Process
import random
import time


def make_tuple(queue):
    num = random.randint(1, 9)
    queue.put(('Hi', num))
    time.sleep(1)
    # Give the 'make_string()' an opportunity to get the tuple, rather than 
    # the 'make_tuple()' snatching it up, immediately after putting it
    # in the queue

    print(queue.get())                  
    # get() signature --> Queue.get([block[, timeout]])
    # By default, get() is blocking and will wait until 
    # an item is available to get from the queue

    # If block flag is True, a timeout can also be specified.

    # If block flag is set to False,
    # get() returns immediately with the retrieved item
    # or if queue is empty, throws the Queue.Empty exception

def make_string(queue):
    tup = queue.get()
    sub_str, num = tup

    result = ''
    for _ in range(num):
        result += sub_str
    
    queue.put(result)


if __name__ == '__main__':
    queue = Queue()
    p1 = Process(target=make_tuple, args=(queue,))
    p2 = Process(target=make_string, args=(queue,))
    p1.start()
    p2.start()

    p1.join()
    p2.join()
    print("All done!!")