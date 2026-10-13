from collections import deque


class RateLimiter:

    def __init__(self,max_request,window_sec):
        self.max_request = max_request
        self.window_sec = window_sec
        self.deque = deque()


    def allow(self,req):

        while self.deque and req - self.window_sec >= 0:
            self.deque.popleft()


        if len(self.deque) < self.max_request:
            self.deque.append(req)
            return True

        return False



rl = RateLimiter(2,10)

print([rl.allow(req) for req in [0,1,2,11]])
