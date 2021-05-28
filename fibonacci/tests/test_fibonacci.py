import pytest

# copied from wikipedia
FIBONACCI_NUMBERS = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]


@pytest.mark.parametrize('n,expected', enumerate(FIBONACCI_NUMBERS))
def test_fibonacci(n, expected):
    '''Test the initial conditions of the recursion'''
    from fibonacci import fibonacci

    assert fibonacci(n) == expected


@pytest.mark.parametrize('n', [-1, -5, -1000])
def test_invalid(n):
    from fibonacci import fibonacci, fibonacci_generator

    with pytest.raises(ValueError):
        fibonacci(n)

    with pytest.raises(ValueError):
        next(fibonacci_generator(n))


def test_generator():
    from fibonacci import fibonacci_generator

    n = len(FIBONACCI_NUMBERS)
    assert list(fibonacci_generator(n)) == FIBONACCI_NUMBERS
