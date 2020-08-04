import pytest

import tests.kernel as tk
import tests.config as cf

from typing import List


LIMIT = 60
EXPECTED_DEVICES = ("m1", "m2", "m3", "m4", "m5", "m6", "m7", "m8")
LOGS_M1 = [ 
    "<INFO> Started",
    "<AUTH> ospf4: Authentication failed for nbr 10.0.0.3 on ve2 - wrong password",
    "<AUTH> ospf5: Authentication failed for nbr 10.0.0.3 on ve2 - wrong authentication code",
    "<AUTH> ospf6: Authentication failed for nbr 10.0.0.3 on ve2 - wrong authentication code"
]

LOGS_M3 = [ 
    "<INFO> Started",
    "<AUTH> ospf4: Authentication failed for nbr 10.0.0.1 on ve1 - wrong password",
    "<AUTH> ospf5: Authentication failed for nbr 10.0.0.1 on ve1 - wrong authentication code",
    "<AUTH> ospf6: Authentication failed for nbr 10.0.0.1 on ve1 - wrong authentication code",
]

LOGS_M6 = [ 
    "<INFO> Started",
    "<AUTH> ospf4: Authentication failed for nbr 10.0.0.8 on ve2 - wrong authentication code",
    "<AUTH> ospf5: Authentication failed for nbr 10.0.0.8 on ve2 - wrong authentication code",
    "<AUTH> ospf6: Authentication failed for nbr 10.0.0.8 on ve2 - wrong authentication code",
]

LOGS_M8 = [ 
    "<INFO> Started",
    "<AUTH> ospf4: Authentication failed for nbr 10.0.0.6 on ve1 - wrong authentication code",
    "<AUTH> ospf5: Authentication failed for nbr 10.0.0.6 on ve1 - wrong authentication code",
    "<AUTH> ospf6: Authentication failed for nbr 10.0.0.6 on ve1 - wrong authentication code",
]


@pytest.mark.skipif(cf.save == False, reason="mode: save")
def test_wait():
    """Wait until the time (limit) runs out"""
    tk.wait(LIMIT)


@pytest.mark.parametrize(
    "exp_devs, exp_messages",
    [
        pytest.param("m1", LOGS_M1),
        pytest.param("m2", []),
        pytest.param("m3", LOGS_M3),
        pytest.param("m4", []),
        pytest.param("m5", []),
        pytest.param("m6", LOGS_M6),
        pytest.param("m7", []),
        pytest.param("m8", LOGS_M8)
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
    tk.test_bird_routes("master4", exp_devs, "master4")


@pytest.mark.parametrize("exp_devs", EXPECTED_DEVICES)
def test_bird_routes_ipv6(exp_devs: str):
    """IPv6: get the content of BIRD tables and check it"""
    tk.test_bird_routes("master6", exp_devs, "master6")
