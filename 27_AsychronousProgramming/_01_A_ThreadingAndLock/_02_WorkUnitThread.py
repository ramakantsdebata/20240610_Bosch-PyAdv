import threading

class FibonacciThread(threading.Thread):
    def __init__(self, num):
        super().__init__()
        self.num= num

    def run(self):
        fib = [0] * (self.num+ 1)
        fib[0] = 0; print(fib[0])
        fib[1] = 1; print(fib[1])
        for i in range(2, self.num+1):
            fib[i] = fib[i-1] + fib[i-2]
            print(fib[i])


myFibTask1 = FibonacciThread(9)
myFibTask2 = FibonacciThread(12)
myFibTask1.start()
myFibTask2.start()
myFibTask1.join()
myFibTask2.join()