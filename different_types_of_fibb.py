from datetime import datetime
from functools import wraps
from functools import reduce
from functools import lru_cache


def time_it(f):

    @wraps(f)
    def wrapper(args):
        start_time = datetime.now()
        f(args)
        end_time = datetime.now()

        elapsed_time = end_time - start_time
        elapsed_time = elapsed_time.microseconds

        return elapsed_time
    return wrapper


@time_it
def fibslow(n):
    if n <= 1:
        return n

    else:
        return fibslow(n-1) + fibslow(n-2)

@time_it
@lru_cache(10)
def fib_with_cache(n):
    if n <= 1:
        return n

    else:
        return fib_with_cache(n-1) + fib_with_cache(n-2)

@time_it
def fib_reduce(n):
    return reduce(lambda x,n: [x[1], x[0]+x[1]], range(n), [0, 1])

@time_it
def my_favourite_fib(n):
    x =0
    y =1
    for el in range(n):
        x, y = y, x+y

    return(x)



print(fibslow(20))
print(fib_with_cache(20))
print(fib_reduce(20))
print(my_favourite_fib(20))