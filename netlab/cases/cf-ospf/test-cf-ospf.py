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


@pytest.mark.skipif(
    mode == "check",
    reason="No need to verify time of convergence during the check mode",
)
def test_wait():
    """Wait until the time (limit) runs out"""
    tk.wait(_LIMIT)


@pytest.mark.parametrize(
    "expected_device", ["m1", "m2", "m3", "m4"],
)
def test_krt_routes(expected_device,):
    """
    Test kernel routes:
    -------------------
         - default parametr :limit: set to the value 60 seconds
    """
    tk.test_krt_routes(expected_device, "ospf")
