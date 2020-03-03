import pytest
import tests.kernel as tk

LIMIT = 60


@pytest.mark.skipif(
    tk.cf.save == False,
    reason="No need to verify time of convergence during the check mode",
)
def test_wait():
    """Wait until the time (limit) runs out"""
    tk.wait(LIMIT)


@pytest.mark.parametrize(
    "expected_device", ["m11", "m21", "m31", "m41"],
)
def test_krt_routes(expected_device,):
    """
    Test kernel routes:
    -------------------
         - default parametr :limit: set to the value 60 seconds
    """
    tk.test_krt_routes("krt", expected_device, "bgp")
