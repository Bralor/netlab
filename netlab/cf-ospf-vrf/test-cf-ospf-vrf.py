import pytest

import tests.kernel as tk
import tests.config as cf

from typing import List


LIMIT = 60
EXPECTED_DEVICES = ("m1", "m2", "m3", "m4", "m5", "m6", "m7", "m8", "m9", "m10")

@pytest.mark.skipif(cf.save == False, reason="mode: save")
def test_wait():
    """Wait until the time (limit) runs out"""
    tk.wait(LIMIT)


@pytest.mark.parametrize(
    "exp_devs, exp_messages",
    [
        pytest.param("m1", []),
        pytest.param("m2", []),
        pytest.param("m3", []),
        pytest.param("m4", []),
        pytest.param("m5", []),
        pytest.param("m6", []),
        pytest.param("m7", []),
        pytest.param("m8", []),
        pytest.param("m9", []),
        pytest.param("m10",[]),
    ],
)
def test_logging(exp_devs: str, exp_messages: List[str]):
    """Check the log files. There should only DBG, INFO and TRACE messages"""
    tk.test_logs(exp_devs, exp_messages)


@pytest.mark.parametrize("exp_devs", EXPECTED_DEVICES)
def test_krt_routes_ipv4(exp_devs: str):
    """IPv4: get the content of KERNEL tables and check it"""
    tk.test_krt_routes("krt4", exp_devs, "IPv4")

def test_krt_routes_ipv4_vrf2():
    tk.test_krt_routes("krt4vrf2", "m1", "IPv4", "200")

def test_krt_routes_ipv4_vrf3():
    tk.test_krt_routes("krt4vrf3", "m1", "IPv4", "300")


@pytest.mark.parametrize("exp_devs", EXPECTED_DEVICES)
def test_krt_routes_ipv4_ospf3(exp_devs: str):
    """IPv4: get the content of KERNEL tables and check it"""
    tk.test_krt_routes("krt5", exp_devs, "IPv4", "100")


@pytest.mark.parametrize("exp_devs", EXPECTED_DEVICES)
def test_krt_routes_ipv6(exp_devs: str):
    """IPv6: get the content of KERNEL tables and check it"""
    tk.test_krt_routes("krt6", exp_devs, "IPv6")

def test_krt_routes_ipv6_vrf2():
    tk.test_krt_routes("krt6vrf2", "m1", "IPv6", "200")

def test_krt_routes_ipv6_vrf3():
    tk.test_krt_routes("krt6vrf3", "m1", "IPv6", "300")


@pytest.mark.parametrize("exp_devs", EXPECTED_DEVICES)
def test_bird_routes_ipv4(exp_devs: str):
    """IPv4: get the content of BIRD tables and check it"""
    tk.test_bird_routes("master4", exp_devs, "master4")

@pytest.mark.parametrize("tab", ("t100v4", "t200v4", "t300v4"))
def test_bird_routes_ipv4_vrfs(tab: str):
    tk.test_bird_routes(tab, "m1", tab)


@pytest.mark.parametrize("exp_devs", EXPECTED_DEVICES)
def test_bird_routes_ipv4_ospf3(exp_devs: str):
    """IPv4: get the content of BIRD tables and check it"""
    tk.test_bird_routes("master5", exp_devs, "master5")


@pytest.mark.parametrize("exp_devs", EXPECTED_DEVICES)
def test_bird_routes_ipv6(exp_devs: str):
    """IPv6: get the content of BIRD tables and check it"""
    tk.test_bird_routes("master6", exp_devs, "master6")

@pytest.mark.parametrize("tab", ("t100v6", "t200v6", "t300v6"))
def test_bird_routes_ipv6_vrfs(tab: str):
    tk.test_bird_routes(tab, "m1", tab)
