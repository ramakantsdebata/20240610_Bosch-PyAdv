import threading

lock : threading.Lock = None

gbl_data = 100


# Acquiring lock for first time
def Foo():
    print("Foo")
    global gbl_data
    if lock.acquire() is True:
        print("Foo: Acquired lock")
        gbl_data += 100
        Bar()
        lock.release()
    else:
        print("Foo: Failed to lock")

# Acquiring lock for second time
def Bar():
    print("Bar")
    global gbl_data
    if lock.acquire(timeout=5) is True:
        print("Bar: Acquired lock")
        gbl_data += 10
        lock.release()
    else:
        print("Bar: Failed to lock")

if __name__ == '__main__':
    # Using simple lock
    lock = threading.Lock()
    t1 = threading.Thread(target=Foo)
    t1.start()
    t1.join()
    print("#" * 80)

    # Using re-entrant lock
    lock = threading.RLock()
    t2 = threading.Thread(target=Foo)
    t2.start()
    t2.join()




