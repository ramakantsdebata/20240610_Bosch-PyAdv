import threading
import time
import random

class ProducerConsumer:
    def __init__(self) -> None:
        self.condition = threading.Condition()
        self.queue = []

    def produce(self):
        for _ in range(10):
            item = random.randint(1, 100)   # Generate random data as the produce
            with self.condition:    
                self.queue.append(item)
                print(f"Produced: {item}")
                self.condition.notify() # Notify the consumer that a new item is available
            time.sleep(random.uniform(0.1, 0.5)) # Simulate production time

    def consume(self):
        for _ in range(10):
            with self.condition:
                while not self.queue:
                    self.condition.wait()
                item = self.queue.pop(0)
                print(f"Consumed: {item}")
            time.sleep(random.uniform(0.1, 0.5))    # Simulate consumption time

    

def main():
    pc = ProducerConsumer()
    producer_thread = threading.Thread(target=pc.produce)
    consumer_thread = threading.Thread(target=pc.consume)

    producer_thread.start()
    consumer_thread.start()

    producer_thread.join()
    consumer_thread.join()

if __name__ == '__main__':
    main()


'''
    ProducerConsumer Class:
        __init__ Method: Initializes the Condition object and an empty list (queue) to hold produced items.
        produce Method: Produces 10 random items, appends each item to the queue, and notifies the consumer thread that a new item is available.
        consume Method: Consumes 10 items from the queue. If the queue is empty, it waits until the producer thread notifies that an item is available.

    Main Function:
        Creates an instance of ProducerConsumer.
        Creates and starts the producer and consumer threads.
        Waits for both threads to finish using join().

    Threading:
        The produce method is run in a separate thread.
        The consume method is run in another separate thread.
        Condition is used to synchronize the producer and consumer threads, ensuring the consumer waits for items to be produced before consuming them.
'''