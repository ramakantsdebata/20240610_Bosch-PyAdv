import threading

def PrintMsg():
    print("Timer Executed!")

if __name__ == '__main__':
    timer = threading.Timer(5.0, PrintMsg)
    timer.start()
    print("Waiting for the timer event...")