def repeat(n):
    def decorator(fn):
        def wrapper(*args, **kwargs):
            print(f"Calling '{fn.__name__}'")
            for _ in range(n):
                fn(*args, **kwargs)
            print(f"Exiting '{fn.__name__}'")
        return wrapper
    return decorator

@repeat(n=3)
def greet(name):
    print(f"Hello {name}!")


greet("Ramakant")