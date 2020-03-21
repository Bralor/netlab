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
    "expected_device", ["m21", "m22", "m23", "m41", "m42", "m43", "m44",],
)
def test_krt_routes(expected_device):
    """
    # Basic test case:
    1. Check the krt tables in a while
    2. Check the status of specific protocols
    """
    tk.test_krt_routes("krt", expected_device, "bgp")


@pytest.mark.skipif(mode == "save", reason="mode: check")
@pytest.mark.parametrize("expected_device", ["m24", "m31", "m32", "m33"])
def test_nodes_with_mismatched_passwords(expected_device):
    results = tk.nodes_with_password(expected_device, "password")
    for protocol in results.values():
        assert "Established" not in protocol.values()


@pytest.mark.skipif(mode == "save", reason="mode: check")
@pytest.mark.parametrize("expected_device", ["m21", "m22", "m41", "m42"])
def test_nodes_with_matching_passwords(expected_device):
    results = tk.nodes_with_password(expected_device, "password")
    for protocol in results.values():
        assert "Established" in protocol.values()
