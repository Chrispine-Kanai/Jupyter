# Decorators modify the behaviour of a function without permanently modifying
# it. It basically wraps another function and since both functions are callable it remains
# callable


import functools


def repeat(num):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num):
                value = func(*args, **kwargs)
            return value
        return wrapper
    return decorator_repeat


@repeat(5)
def function(name):
    print(f"{name}")


function("Python")
