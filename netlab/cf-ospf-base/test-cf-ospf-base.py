import pytest

import tests.kernel as tk
import tests.config as cf


LIMIT = 60
EXPECTED_DEVICES = ("m1", "m2", "m3", "m4", "m5", "m6", "m7", "m8")


@pytest.mark.skipif(cf.save == False, reason="mode: save")
def test_wait():
    """Wait until the time (limit) runs out"""
    tk.wait(LIMIT)


@pytest.mark.parametrize("exp_devs", EXPECTED_DEVICES)
def test_krt_routes_ipv4(exp_devs: str):
    """IPv4: get the content of KERNEL tables and check it"""
    tk.test_krt_routes("krt", exp_devs)


@pytest.mark.parametrize("exp_devs", EXPECTED_DEVICES)
def test_krt_routes_ipv6(exp_devs: str):
    """IPv6: get the content of KERNEL tables and check it"""
    tk.test_krt_routes("krt", exp_devs, 6)


@pytest.mark.parametrize("exp_devs", EXPECTED_DEVICES)
def test_bird_routes_ipv4(exp_devs: str):
    """IPv4: get the content of BIRD tables and check it"""
    tk.test_bird_routes("bird", exp_devs)


@pytest.mark.parametrize("exp_devs", EXPECTED_DEVICES)
def test_bird_routes_ipv6(exp_devs: str):
    """IPv6: get the content of BIRD tables and check it"""
    tk.test_bird_routes("bird", exp_devs, 6)
