# The "timeit" module lets you measure the execution
# time of small bits of Python code

import timeit

timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)

timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)

timeit.timeit('"-".join(map(str, range(100)))', number=10000)

