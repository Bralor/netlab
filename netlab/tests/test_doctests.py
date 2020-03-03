import doctest

VAR1 = 1


def test_func():
    """
    # sample of doctest:
    >>> sum = 2 + VAR1
    >>> print(sum)
    3
    """


if __name__ == "__main__":
    doctest.testmod()
