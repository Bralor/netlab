import pytest
import tests.kernel as tk

LIMIT = 60


@pytest.mark.skipif(tk.cf.save == False, reason="mode: save")
def test_wait():
    """Wait until the time (limit) runs out"""
    tk.wait(LIMIT)


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
    tk.test_krt_routes("krt", expected_device, "bgp")
