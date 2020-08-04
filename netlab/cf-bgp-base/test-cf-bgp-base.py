import pytest

import tests.kernel as tk
import tests.config as cf

from typing import List


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


@pytest.mark.skipif(cf.save == False, reason="mode: save")
def test_wait():
    """Wait until the time (limit) runs out"""
    tk.wait(LIMIT)


@pytest.mark.parametrize(
    "exp_devs, exp_messages",
    [
        pytest.param("m11", []),
        pytest.param("m12", []),
        pytest.param("m13", []),
        pytest.param("m14", []),
        pytest.param("m21", []),
        pytest.param("m22", []),
        pytest.param("m23", []),
        pytest.param("m24", []),
        pytest.param("m31", []),
        pytest.param("m32", []),
        pytest.param("m33", []),
        pytest.param("m34", []),
        pytest.param("m41", []),
        pytest.param("m42", []),
        pytest.param("m43", []),
        pytest.param("m44", []),
    ],
)
def test_logging(exp_devs: str, exp_messages: List[str]):
    """Check the log files. There should only DBG, INFO and TRACE messages"""
    tk.test_logs(exp_devs, exp_messages)


@pytest.mark.parametrize("exp_devs", EXPECTED_DEVICES)
def test_krt_routes_ipv4(exp_devs: str):
    """IPv4: get the content of KERNEL tables and check it"""
    tk.test_krt_routes("krt4", exp_devs, "IPv4")


@pytest.mark.parametrize("exp_devs", EXPECTED_DEVICES)
def test_krt_routes_ipv6(exp_devs: str):
    """IPv6: get the content of KERNEL tables and check it"""
    tk.test_krt_routes("krt6", exp_devs, "IPv6")


@pytest.mark.parametrize("exp_devs", EXPECTED_DEVICES)
def test_bird_routes_ipv4(exp_devs: str):
    """IPv4: get the content of BIRD tables and check it"""
    tk.test_bird_routes("master4", exp_devs, "master4", "primary")


@pytest.mark.parametrize("exp_devs", EXPECTED_DEVICES)
def test_bird_routes_ipv6(exp_devs: str):
    """IPv6: get the content of BIRD tables and check it"""
    tk.test_bird_routes("master6", exp_devs, "master6", "primary")
