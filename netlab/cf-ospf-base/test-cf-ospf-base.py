import pytest
import tests.kernel as tk

LIMIT = 60
EXPECTED_DEVICES = ("m1", "m2", "m3", "m4", "m5", "m6", "m7", "m8")


@pytest.mark.skipif(tk.cf.save == False, reason="mode: save")
def test_wait():
    """Wait until the time (limit) runs out"""
    tk.wait(LIMIT)


@pytest.mark.parametrize("exp_devs", EXPECTED_DEVICES)
def test_krt_routes(exp_devs):
    """Get the content of KERNEL tables and check it"""
    tk.test_krt_tables("krt", exp_devs)


@pytest.mark.parametrize("exp_devs", EXPECTED_DEVICES)
def test_bird_routes(exp_devs):
    """Get the content of BIRD tables and check it"""
    tk.test_bird_tables("bird", exp_devs)
