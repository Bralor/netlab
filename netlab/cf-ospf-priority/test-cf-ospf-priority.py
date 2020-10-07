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
    tk.test_krt_routes("krt4", exp_devs, "inet")


@pytest.mark.parametrize("exp_devs", EXPECTED_DEVICES)
def test_krt_routes_ipv4_ospf3(exp_devs: str):
    """IPv4: get the content of KERNEL tables and check it"""
    tk.test_krt_routes("krt5", exp_devs, "inet", "100")


@pytest.mark.parametrize("exp_devs", EXPECTED_DEVICES)
def test_krt_routes_ipv6(exp_devs: str):
    """IPv6: get the content of KERNEL tables and check it"""
    tk.test_krt_routes("krt6", exp_devs, "inet6")


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


@pytest.mark.parametrize("exp_devs", EXPECTED_DEVICES)
def test_ospf_neighbors_ipv4(exp_devs: str):
    """IPv4: get the status of neihbors and check it"""
    tk.test_ospf_neighbors(key="neighbor-cf1", dev=exp_devs, protocol="ospf4")


@pytest.mark.parametrize("exp_devs", EXPECTED_DEVICES)
def test_ospf_neighbors_ipv5(exp_devs: str):
    """IPv6: get the status of neihbors and check it"""
    tk.test_ospf_neighbors(key="neighbor-cf1", dev=exp_devs, protocol="ospf5")


@pytest.mark.parametrize("exp_devs", EXPECTED_DEVICES)
def test_ospf_neighbors_ipv6(exp_devs: str):
    """IPv6: get the status of neihbors and check it"""
    tk.test_ospf_neighbors(key="neighbor-cf1", dev=exp_devs, protocol="ospf6")


@pytest.mark.parametrize("exp_devs", ["m3", "m4", "m5", "m6"])
def test_ospf_reconfigure(exp_devs: str):
    """Reconfigure some devices with config file 'bird_2.conf'"""
    tk.run_configure(exp_devs, "bird_2.conf")


@pytest.mark.skipif(cf.save == False, reason="mode: save")
def test_wait_after_reconf():
    """Wait until the time (limit) runs out"""
    tk.wait(60)


@pytest.mark.parametrize("exp_devs", EXPECTED_DEVICES)
def test_bird_routes_ipv4_after_reconf(exp_devs: str):
    """IPv4: get the content of BIRD tables and check it"""
    tk.test_bird_routes("master4-cf2", exp_devs, "master4")


@pytest.mark.parametrize("exp_devs", EXPECTED_DEVICES)
def test_bird_routes_ipv4_ospf3_after_reconf(exp_devs: str):
    """IPv4: get the content of BIRD tables and check it"""
    tk.test_bird_routes("master5-cf2", exp_devs, "master5")


@pytest.mark.parametrize("exp_devs", EXPECTED_DEVICES)
def test_bird_routes_ipv6_after_reconf(exp_devs: str):
    """IPv6: get the content of BIRD tables and check it"""
    tk.test_bird_routes("master6-cf2", exp_devs, "master6")


@pytest.mark.parametrize("exp_devs", EXPECTED_DEVICES)
def test_ospf_neighbors_ospf4_after_reconf(exp_devs: str):
    """IPv4: After reconfiguration check the neighbor\'s tables"""
    tk.test_ospf_neighbors(key="neighbor-cf2", dev=exp_devs, protocol="ospf4")


@pytest.mark.parametrize("exp_devs", EXPECTED_DEVICES)
def test_ospf_neighbors_ospf5_after_reconf(exp_devs: str):
    """IPv6: After reconfiguration check the neighbor\'s tables"""
    tk.test_ospf_neighbors(key="neighbor-cf2", dev=exp_devs, protocol="ospf5")


@pytest.mark.parametrize("exp_devs", EXPECTED_DEVICES)
def test_ospf_neighbors_ospf6_after_reconf(exp_devs: str):
    """IPv6: After reconfiguration check the neighbor\'s tables"""
    tk.test_ospf_neighbors(key="neighbor-cf2", dev=exp_devs, protocol="ospf6")


def test_different_neighbors_table():
    expected_addresses = ['10.0.0.3', '10.0.0.5', '10.0.0.6']
    file1 = tk.read_file("cf-ospf-priority/data/neighbor-cf1-ospf4-m4")
    file2 = tk.read_file("cf-ospf-priority/data/neighbor-cf2-ospf4-m4")

    different_addresses = [
        line.split("\t", maxsplit=1)[0].strip()
        for index, line in enumerate(file1)
        if file1[index] != file2[index]
    ]
    assert expected_addresses == different_addresses


