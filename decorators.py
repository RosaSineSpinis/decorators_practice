import functools #keep information which fun inside decorator is used
import time


def deco_fun(fun):
    def wrapper():
        print("wrapper before fun1")
        fun()
        print("wrapper after fun1")
    return wrapper


@deco_fun
def fun1():
    print("fun1 is working ")

################################
def deco_arg(fun):
    @functools.wraps(fun)
    def wrapper(*args, **kwargs):
        print("dec_arg")
        return fun(*args, **kwargs)
        print("")
    return wrapper

@deco_arg
def fun2(str, x):
    print("fun2 is working " + str)
    return x*2

print(fun2("str", 2))
################################

def timer(fun):
    """print run time of the decorated function"""
    @functools.wraps(fun)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        sum = fun(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {fun.__name__!r} in {run_time:.4f} secs")
        return sum
    return wrapper_timer

@timer
def func3(n):
    for x in range(n):
        x=x+x
    return x


print("sum " ,func3(10))
print("sum ", func3(10000000))