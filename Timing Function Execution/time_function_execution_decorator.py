import time
from functools import wraps



def timeit(fun):

    @wraps(fun)
    def wrapping_fun(*args,**kwargs):

        start = time.perf_counter()
        fun(*args,**kwargs)
        print(f'Time taken: {time.perf_counter()-start:.3f}')

    return wrapping_fun

@timeit
def functionToCheck():
    time.sleep(2)
    



functionToCheck()
