from threading import Semaphore, BoundedSemaphore

def RegSemaphore():
    print("\nRegular Semaphore")
    s1 = Semaphore(5)

    s1.acquire()

    # Then you do whatever sensitive thing needed to be restricted to five threads.

    # When you're finished, you release the semaphore, and it goes back to 5.
    s1.release()


    # If you release it without acquiring it first.
    s1.release()

    # The counter is now 6
    print(s1._value)  # => 6

def Bound_Semaphore():
    print("\n\nBounded Semaphore")
    # Use Bounded Semaphore, if unbounded release is undesirable

    s2 = BoundedSemaphore(5)  # Start at 5.

    s2.acquire()  # Lower to 4.

    s2.release()  # Go back to 5.

    try:
        s2.release()  # Try to raise to 6, above starting value.
    except ValueError:
        print('As expected, it complained.')

if __name__ == "__main__":
    RegSemaphore()
    Bound_Semaphore()