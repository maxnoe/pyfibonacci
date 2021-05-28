from functools import lru_cache


@lru_cache()
def fibonacci(n):
    '''
    Calculate the nth fibonacci number using recursion and memoization

    Examples
    --------
    >>> fibonacci(7)
    13
    '''
    if n < 0:
        raise ValueError(f'n must be >= 0, got {n}')

    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_generator(n):
    '''
    A generator for fibonacci numbers.
    '''
    if n < 0:
        raise ValueError(f'n must be >= 0, got {n}')

    n0 = 0
    yield n0

    if n == 0:
        return

    n1 = 1
    yield n1

    if n == 1:
        return

    for _ in range(2, n):
        n0, n1 = n1, n0 + n1
        yield n1
