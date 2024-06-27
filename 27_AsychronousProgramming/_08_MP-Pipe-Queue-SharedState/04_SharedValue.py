import ctypes
from multiprocessing import Value, Process, Lock

def example_function(shared_int, shared_bool, shared_long):
    # Modify shared_int
    with shared_int.get_lock():  # Acquire lock before modifying
        shared_int.value += 1

    # shared_bool was specified without a lock
    shared_bool.value = not shared_bool.value

    # Modify shared_long
    with shared_long.get_lock():  # Acquire lock before modifying
        shared_long.value += 5

if __name__ == "__main__":
    # Shared integer, defaults to 0
    shared_int = Value('i', 0)  # 'i' stands for int

    # Shared boolean, defaulting to False, unsynchronized
    shared_bool = Value(ctypes.c_bool, False, lock=False)  # No synchronization

    # Shared long integer, defaults to 0, with a lock specified
    shared_long = Value('l', 0)  # 'l' stands for long

    processes = [Process(target=example_function, args=(shared_int, shared_bool, shared_long)) for _ in range(5)]

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    print("shared_int:", shared_int.value)
    print("shared_bool:", shared_bool.value)
    print("shared_long:", shared_long.value)

