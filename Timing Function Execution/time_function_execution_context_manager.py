from contextlib import contextmanager
import time


@contextmanager
def timit():
    start = time.perf_counter()
    yield start
    print(f'Time taken:{time.perf_counter()-start:.3f}')


with timit() as start:
##    print(f'Time started:{start}')
    time.sleep(2)
    
