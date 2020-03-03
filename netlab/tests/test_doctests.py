import doctest

from kernel import modify_command


def test_func():
    """
    # sample of doctest:
    >>> sum = 2 + 1
    >>> print(sum)
    3
    """


def test_modify_command():
    """
    # sample of existing function
    >>> modify_command('mn')
    'cd mn && sudo ./birdc -l show protocols'
    """


if __name__ == "__main__":
    doctest.testmod()
