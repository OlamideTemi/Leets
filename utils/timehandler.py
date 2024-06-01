import time

def timeHandlerWrapper(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        period = end-start
        print(f"Code runtime -> {period}")
        return result
    return wrapper
