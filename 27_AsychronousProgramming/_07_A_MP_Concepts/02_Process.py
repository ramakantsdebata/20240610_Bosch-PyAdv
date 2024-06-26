import multiprocessing

def do_some_work(val):
    print("doing some work in process")
    print(f"echo: {val}")
    return

if __name__ == '__main__':
    val = "text"
    t = multiprocessing.Process(target=do_some_work, args=(val,))
    t.start()
    t.join()


'''
class multiprocessing.Process(group=None,
                                target=None,
                                name=None,
                                args=(),
                                kwargs={},
                                daemon=None)
'''
