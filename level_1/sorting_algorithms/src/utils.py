import time
import sys


def measure_time_complexity(func, list):
    start_time = time.time()
    func(list)
    end_time = time.time()
    return end_time - start_time

def measure_space_complexity(func, list):
    start_memory = sys.getsizeof(list)
    func(list)
    end_memory = sys.getsizeof(list)
    return end_memory - start_memory