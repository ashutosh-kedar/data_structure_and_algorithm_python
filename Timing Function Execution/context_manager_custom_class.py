
import time

class Timeit:

    def __init__(self,title):
        self.title = title
        self.start = None


    def __enter__(self):
        self.start = time.perf_counter()

    def __exit__(self,exc_type,exc_value,exc_tb):
        print(f'Time taken: {time.perf_counter()-self.start}')




with Timeit('Timing') as tt:
    time.sleep(2)
