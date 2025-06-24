import time

def time_to_exec(function) -> float:
    start_time = time.time()
    function()
    end_time = time.time()
    return end_time - start_time

def dummy_function():
    for number in range(100000000):
        number = number * number

print(time_to_exec(dummy_function))