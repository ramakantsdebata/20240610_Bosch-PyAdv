def log_with_level(level):
    def decorator(fn):
        def wrapper(*args, **kwargs):
            print(f"[{level.upper()}] Calling '{fn.__name__}'")
            result = fn(*args, **kwargs)
            return result
        return wrapper
    return decorator

@log_with_level("info")
def greet(name):
    print(f"Hello {name}!")

@log_with_level("debug")
def add(a, b):
    return a+b

@log_with_level("info")
def sub(a, b):
    return a-b

print(add(1, 2))
print(sub(2, 1))
greet("Manish")