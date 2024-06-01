import functools

def log_params(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        params = {f'arg{index}': type(arg).__name__ for index, arg in enumerate(args)}
        params.update({key: type(value).__name__ for key, value in kwargs.items()})
        print(params)
        return func(*args, **kwargs)
    return wrapper

@log_params
def my_function(a, b, c=3):
    return a + b + c

result = my_function(1, 2, c=3)
print(result)