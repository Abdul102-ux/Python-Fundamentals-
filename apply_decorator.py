
def decorator_func(func):
    def wrapper(*args, **kwargs):
        print("Decorator Applied")
        return func(*args, **kwargs)
    return wrapper

@decorator_func
def apply_decorator():
    return "Function executed"


print(apply_decorator())
