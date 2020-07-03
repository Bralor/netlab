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
def test_logging(exp_devs: str):
    """Check the log files. There should only DBG, INFO and TRACE messages"""
    tk.read_logs(exp_devs, "bird.log")


@pytest.mark.parametrize("exp_devs", EXPECTED_DEVICES)
def test_krt_routes_ipv4(exp_devs: str):
    """IPv4: get the content of KERNEL tables and check it"""
    tk.test_krt_routes("krt4", exp_devs, "IPv4")


@pytest.mark.parametrize("exp_devs", EXPECTED_DEVICES)
def test_krt_routes_ipv4_ospf3(exp_devs: str):
    """IPv4: get the content of KERNEL tables and check it"""
    tk.test_krt_routes("krt5", exp_devs, "IPv4", "100")


@pytest.mark.parametrize("exp_devs", EXPECTED_DEVICES)
def test_krt_routes_ipv6(exp_devs: str):
    """IPv6: get the content of KERNEL tables and check it"""
    tk.test_krt_routes("krt6", exp_devs, "IPv6")


@pytest.mark.parametrize("exp_devs", EXPECTED_DEVICES)
def test_bird_routes_ipv4(exp_devs: str):
    """IPv4: get the content of BIRD tables and check it"""
    tk.test_bird_routes("master4", exp_devs, "master4")


@pytest.mark.parametrize("exp_devs", EXPECTED_DEVICES)
def test_bird_routes_ipv4_ospf3(exp_devs: str):
    """IPv4: get the content of BIRD tables and check it"""
    tk.test_bird_routes("master5", exp_devs, "master5")


@pytest.mark.parametrize("exp_devs", EXPECTED_DEVICES)
def test_bird_routes_ipv6(exp_devs: str):
    """IPv6: get the content of BIRD tables and check it"""
    tk.test_bird_routes("master6", exp_devs, "master6")
