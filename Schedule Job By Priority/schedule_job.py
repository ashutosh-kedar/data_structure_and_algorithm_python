import heapq

jobs = [(3, "backup"), (1, "deploy"), (2, "test")]



def schedule_jobs(jobs):

    heapq.heapify(jobs)

    while jobs:

        _,name = heapq.heappop(jobs)

        print(name)



schedule_jobs(jobs)


