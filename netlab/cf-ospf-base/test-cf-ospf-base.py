import pytest

import tests.config as cf
from tests.kernel import wait
from tests.kernel import test_krt_routes as tkr
from tests.kernel import test_bird_routes as tbr


LIMIT = 60
EXPECTED_DEVICES = ("m1", "m2", "m3", "m4", "m5", "m6", "m7", "m8")


@pytest.mark.skipif(cf.save == False, reason="mode: save")
def test_wait():
    """Wait until the time (limit) runs out"""
    wait(LIMIT)


@pytest.mark.parametrize("exp_devs", EXPECTED_DEVICES)
def test_krt_routes(exp_devs):
    """Get the content of KERNEL tables and check it"""
    tkr("krt", exp_devs)


@pytest.mark.parametrize("exp_devs", EXPECTED_DEVICES)
def test_bird_routes(exp_devs):
    """Get the content of BIRD tables and check it"""
    tbr("bird", exp_devs)
