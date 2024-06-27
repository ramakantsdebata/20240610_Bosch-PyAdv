import multiprocessing
import time
import random

# Producer-Consumer using multiprocessing.Pipe
def producer(conn):
    for _ in range(5):
        item = random.randint(1, 100)
        print(f'Producer: producing item {item}')
        conn.send(item)
        time.sleep(random.uniform(0.1, 0.5))

    # Signal to consumer that production is done
    conn.send(None)
    conn.close()

def consumer(conn):
    while True:
        item = conn.recv()
        if item is None:
            break
        print(f'Consumer: consuming item {item}')
        time.sleep(random.uniform(0.1, 0.5))

def main():
    prod_conn, cons_conn = multiprocessing.Pipe()

    p1 = multiprocessing.Process(target=producer, args=(prod_conn,))
    p2 = multiprocessing.Process(target=consumer, args=(cons_conn,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

if __name__ == "__main__":
    main()
