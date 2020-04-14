import os
import sys
import pickle
import pytest
from inspect import getsourcefile

current_dir = os.path.dirname(os.path.abspath(getsourcefile(lambda: 0)))
sys.path.insert(0, current_dir.rsplit(os.path.sep, 2)[0])
import tests.kernel as tk

sys.path.pop(0)

with open("common/runtest_args.pckl", "rb") as args_file:
    testdir, mode = pickle.load(args_file)

LIMIT = 60
EXPECTED_DEVICES = (
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
)


@pytest.mark.skipif(mode == "check", reason="mode: save")
def test_wait():
    """Wait until the time (limit) runs out"""
    tk.wait(LIMIT)


@pytest.mark.skipif(mode == "check", reason="mode: save")
@pytest.mark.parametrize("exp_devs", EXPECTED_DEVICES)
def test_save_krt_tables(exp_devs):
    tk.save_krt_routes(exp_devs, testdir)


@pytest.mark.skipif(mode == "save", reason="mode: check")
@pytest.mark.parametrize("exp_devs", EXPECTED_DEVICES)
def test_check_krt_routes_timeout(exp_devs):
    tk.check_krt_routes_timeout(exp_devs, testdir)
