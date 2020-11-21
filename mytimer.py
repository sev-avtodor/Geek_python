import time

reps = 1000
repslist = range(reps)


def timer(func, *pargs, **kwargs):
    start = time.clock()
    for i in repslist:
        ret = func(*pargs, **kwargs)
    elapsed = time.clock() - start
    return (elapsed, ret)
