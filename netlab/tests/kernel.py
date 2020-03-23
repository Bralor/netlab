import os
import sys
import pickle
import subprocess
from time import sleep


def test_krt_routes(dev, protocol):
    tdir, mod = load_args_from_file()
    if mod == "save":
        save_krt_routes(dev, tdir)
    else:
        check_krt_routes_timeout(dev, tdir)
        check_protocol_state(dev, protocol)


def wait(sec: int) -> None:
    sleep(sec)


def load_args_from_file():
    with open("common/runtest_args.pckl", "rb") as args_file:
        return pickle.load(args_file)


def modify_command(dev: str) -> str:
    return f"cd {dev} && sudo ./birdc -l show protocols"


def get_attributes_from_stdout(data: str, protocol: str) -> list:
    return [line.split() for line in data.split("\n") if line.startswith(protocol)]


def check_running_ospf(data: list) -> None:
    assert "Running" in data


def check_established_bgp(data: list) -> None:
    assert "Established" in data


def save_stdout(cmd: str) -> str:
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    proc_stdout = process.communicate()[0].strip()
    return proc_stdout.decode("utf-8")


def read_write_routes(name: str, mode: str, content: str = None) -> None:
    with open(name, mode) as txt:
        if mode == "w":
            txt.write(content)
        elif mode == "r":
            return txt.read()


def save_krt_routes(dev: str, procotol: str, ip: int = 4) -> None:
    """Get the tables, process tables and save them"""
    filename = f"{procotol}/data/krt-{dev}"
    table_content = save_stdout(f"sudo ip netns exec {dev} ip -{ip} route show")
    read_write_routes(filename, mode="w", content=table_content)


def check_krt_routes_timeout(dev, tdir, timeout=60):
    for sec in range(timeout):
        if check_krt_routes(dev, tdir):
            assert True
        elif sec == timeout - 1:
            assert False
        else:
            sleep(1)


def check_krt_routes(dev: str, protocol: str, ip: int = 4) -> bool:
    """Check the content of actual tables and the original"""
    filename = f"{protocol}/data/krt-{dev}"
    mn_table_cont = save_stdout(f"ip netns exec {dev} ip -{ip} route show").split("\n")
    content = read_write_routes(filename, mode="r").split("\n")

    for _ in mn_table_cont:
        return mn_table_cont == content


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
    clean_str = get_attributes_from_stdout(decoded, protocol)

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
    cleaned = get_attributes_from_stdout(decoded, protocol)
    return {str(index): {lst[0]: lst[-1]} for index, lst in enumerate(cleaned)}
