import os
import sys
import subprocess
from time import sleep
from inspect import getsourcefile

current_dir = os.path.dirname(os.path.abspath(getsourcefile(lambda: 0)))
sys.path.insert(0, current_dir[: current_dir.rfind(os.path.sep)])

import tests.config as cf


def wait(sec):
    sleep(sec)


def save_krt_routes(key, dev, ip=4):
    """Get the tables and process them as referencial data"""
    filename = f"{cf.datadir}/{key}-{dev}"
    table_content = save_stdout(f"sudo ip netns exec {dev} ip -{ip} route show")
    write_krt_routes(filename, table_content)


def write_krt_routes(name, content):
    with open(name, "w") as txt:
        txt.write(content)


def read_krt_routes(name):
    with open(name, "r") as txt:
        return txt.read().split("\n")


def check_krt_routes(key, dev, ip=4):
    """Check the content of actual tables and the original"""
    filename = f"{cf.datadir}/{key}-{dev}"
    mn_table_cont = save_stdout(f"ip netns exec {dev} ip -{ip} route show").split("\n")
    content = read_krt_routes(filename)

    for _ in mn_table_cont:
        return mn_table_cont == content


def check_krt_routes_timeout(key, dev, timeout=60):
    for sec in range(timeout):
        if check_krt_routes(key, dev):
            assert True
        elif sec == timeout - 1:
            assert False
        else:
            sleep(1)


def modify_command(dev: str) -> str:
    return f"cd {dev} && sudo ./birdc -l show protocols"


def save_stdout(cmd: str) -> str:
    """Run the command :cmd: and return it as variable (stdout)"""
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    proc_stdout = process.communicate()[0].strip()
    return proc_stdout.decode("utf-8")


def get_attributes_from_output(data: str, protocol: str) -> list:
    """Parse the string from parameter and return list"""
    return [line.split() for line in data.split("\n") if line.startswith(protocol)]


def check_protocol_state(dev: str, protocol: str) -> None:
    """
    1. Modify the specified bash command with proper variable
    2. Send bash command into the function and return output as str
    3. Collect all desirable lines into single list
    4. If the name of the protocol is "ospf", run OSPF checker
    5. ... is "bgp", run BGP checker
    """
    command = modify_command(dev)
    decoded = save_stdout(command)
    clean_str = get_attributes_from_output(decoded, protocol)

    for line in clean_str:
        if protocol == "ospf":
            check_running_ospf(line)

        elif protocol == "bgp":
            check_established_bgp(line)


def check_nodes_with_password(dev: str, protocol: str) -> dict:
    """
    1. Modify the specified bash command with proper variable
    2. Send bash command into the function and return output as str
    3. Collect all the protocol with "password"
    4. Return dictionary with pairs - name: state
    """
    command = modify_command(dev)
    decoded = save_stdout(command)
    cleaned = get_attributes_from_output(decoded, protocol)
    return {str(index): {lst[0]: lst[-1]} for index, lst in enumerate(cleaned)}


def check_running_ospf(data: list) -> None:
    assert "Running" in data


def check_established_bgp(data: list) -> None:
    assert "Established" in data


def test_krt_routes(key, dev, protocol):
    if cf.save:
        save_krt_routes(key, dev)
    else:
        check_krt_routes_timeout(key, dev)
        check_protocol_state(dev, protocol)
