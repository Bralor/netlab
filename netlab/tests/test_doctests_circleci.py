import os
import doctest
import subprocess

from kernel import save_stdout
from kernel import modify_command
from kernel import read_write_routes


def test_modify_command():
    """
    # sample of existing function
    >>> modify_command("m_test")
    'cd m_test && sudo ./birdc -l show protocols'
    """


def test_write_krt_route():
    """
    # testing function write_krt_routes():
    >>> write_krt_read_write_routes(filename:="tests/krt_m_test", mode="w",content='')
    >>> bool(filename.split('/')[1] in os.listdir("tests"))
    True
    """


def test_output_with_password():
    """
    # Check the protocols from BIRD. If there is name with suffix "pswd",
    # get the information about status.
    >>> ebgp_matches = [\
        ['ebgp4_pswd', 'BGP', '---', 'start', '08:22:05.632', 'Connect'], \
        ['ebgp4_pswd', 'BGP', '---', 'start', '08:23:02.442', 'Connect'] \
        ]
    >>> for i, lst in enumerate(ebgp_matches):
    ...     print({lst[0]: lst[-1]})
    {'ebgp4_pswd': 'Connect'}
    {'ebgp4_pswd': 'Connect'}
    """


def test_correct_assertion():
    """
    # Return assertion if the status has not "Established" value
    
    >>> results = {'m13': {'ebgp4_pswd': 'Connect'}}
    >>> poi = results['m13']['ebgp4_pswd']
    >>> assert poi == 'Connect'
    """


def test_incorrect_assertion():
    """
    # Return assertion if the status has not "Established" value

    >>> results = {'m13': {'ebgp4_pswd': 'Established'}}
    >>> poi = results['m13']['ebgp4_pswd']
    >>> assert poi == 'Connect'
    Traceback (most recent call last):
      File "/usr/lib/python3.6/doctest.py", line 1330, in __run
        compileflags, 1), test.globs)
      File "<doctest __main__.test_incorrect_assertion[2]>", line 1, in <module>
        assert poi == 'Connect'
    AssertionError
    """


if __name__ == "__main__":
    doctest.testmod()
