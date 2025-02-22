import pytest

import tests.kernel as tk
import tests.config as cf

LIMIT = 60
EXPECTED_DEVICES = ("m1", "m2", "m3", "m4", "m5", "m6", "m7", "m8", "m9", "m10")


@pytest.mark.skipif(cf.save == False, reason="mode: save")
def test_wait():
    """Wait until the time (limit) runs out"""
    tk.wait(LIMIT)


@pytest.mark.parametrize("exp_devs", EXPECTED_DEVICES)
def test_krt_routes_ipv4(exp_devs: str):
    """IPv4: get the content of KERNEL tables and check it"""
    tk.test_krt_routes("krt4", exp_devs, "inet")

def test_krt_routes_ipv4_vrf2():
    tk.test_krt_routes("krt4vrf2", "m1", "inet", "200")

def test_krt_routes_ipv4_vrf3():
    tk.test_krt_routes("krt4vrf3", "m1", "inet", "300")


@pytest.mark.parametrize("exp_devs", EXPECTED_DEVICES)
def test_krt_routes_ipv6(exp_devs: str):
    """IPv6: get the content of KERNEL tables and check it"""
    tk.test_krt_routes("krt6", exp_devs, "inet6")

def test_krt_routes_ipv6_vrf2():
    tk.test_krt_routes("krt6vrf2", "m1", "inet6", "200")

def test_krt_routes_ipv6_vrf3():
    tk.test_krt_routes("krt6vrf3", "m1", "inet6", "300")


@pytest.mark.parametrize("exp_devs", EXPECTED_DEVICES)
def test_bird_routes_ipv4(exp_devs: str):
    """IPv4: get the content of BIRD tables and check it"""
    tk.test_bird_routes("master4", exp_devs, "master4")

@pytest.mark.parametrize("tab", ("t100v4", "t200v4", "t300v4"))
def test_bird_routes_ipv4_vrfs(tab: str):
    tk.test_bird_routes(tab, "m1", tab)


@pytest.mark.parametrize("exp_devs", EXPECTED_DEVICES)
def test_bird_routes_ipv6(exp_devs: str):
    """IPv6: get the content of BIRD tables and check it"""
    tk.test_bird_routes("master6", exp_devs, "master6")

@pytest.mark.parametrize("tab", ("t100v6", "t200v6", "t300v6"))
def test_bird_routes_ipv6_vrfs(tab: str):
    tk.test_bird_routes(tab, "m1", tab)
