import os
import sys
import pickle
import pytest
from inspect import getsourcefile

current_dir = os.path.dirname(os.path.abspath(getsourcefile(lambda: 0)))
sys.path.insert(0, current_dir.rsplit(os.path.sep, 2)[0])
import tests.kernel as tk

sys.path.pop(0)


_LIMIT = 60

with open("common/runtest_args.pckl", "rb") as args_file:
    testdir, mode = pickle.load(args_file)


@pytest.mark.skipif(mode == "check", reason="mode: save")
def test_wait():
    """Wait until the time (limit) runs out"""
    tk.wait(_LIMIT)


@pytest.mark.parametrize(
    "expected_device",
    [
        "m11",
        "m12",
        "m13",
        "m14",
        "m21",
        "m22",
        "m23",
        "m24",
        "m31",
        "m32",
        "m33",
        "m34",
        "m41",
        "m42",
        "m43",
        "m44",
    ],
)
def test_krt_routes(expected_device):
    """
    # Basic test case:
    1. Check the krt tables in a while
    2. Check the status of specific protocols
    """
    tk.test_krt_routes(expected_device, "bgp")
