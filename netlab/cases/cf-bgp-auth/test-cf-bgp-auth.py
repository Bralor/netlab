import pytest
import tests.kernel as tk

LIMIT = 60


@pytest.mark.skipif(tk.cf.save == False, reason="mode: save")
def test_wait():
    """Wait until the time (limit) runs out"""
    tk.wait(LIMIT)


@pytest.mark.parametrize(
    "expected_device", ["m21", "m22", "m23", "m41", "m42", "m43", "m44",],
)
def test_krt_routes(expected_device):
    """
    # Basic test case:
    1. Check the krt tables in a while
    2. Check the status of specific protocols
    """
    tk.test_krt_routes("krt", expected_device, "bgp")


@pytest.mark.skipif(tk.cf.save == True, reason="mode: check")
@pytest.mark.parametrize("expected_device", ["m24", "m31", "m32", "m33"])
def test_nodes_with_mismatched_passwords(expected_device):
    results = tk.nodes_with_password(expected_device, "password")
    for protocol in results.values():
        assert "Established" not in protocol.values()


@pytest.mark.skipif(tk.cf.save == True, reason="mode: check")
@pytest.mark.parametrize("expected_device", ["m21", "m22", "m41", "m42"])
def test_nodes_with_matching_passwords(expected_device):
    results = tk.nodes_with_password(expected_device, "password")
    for protocol in results.values():
        assert "Established" in protocol.values()

