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


@pytest.mark.skipif(mode == "save", reason="mode: check")
def test_checking_wait():
    """
    Temporary solution. Test are failing without this function.
    The state of specific protocols return "Alone". They need a while for connection
    """
    tk.wait(10)


@pytest.mark.parametrize(
    "expected_device", ["m1", "m2", "m3", "m4", "m5", "m6", "m7", "m8", "m9", "m10"],
)
def test_krt_routes(expected_device):
    """Testing of kernel route tables"""
    tk.test_krt_routes(expected_device, "ospf")
