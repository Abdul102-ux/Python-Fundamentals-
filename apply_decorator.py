
def decorator_func(func):
    def wrapper(*args, **kwargs):
        print("Decorator Applied")
        return func(*args, **kwargs)
    return wrapper

@decorator_func
def apply_decorator():
    return "Function executed"


if __name__ == "__main__":
    print(apply_decorator())  
