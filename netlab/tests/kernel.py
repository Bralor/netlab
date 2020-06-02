import os
import sys
import time
import subprocess

import tests.config as cf


def test_krt_routes(key: str, dev: str, ip: int = 4) -> None:
    if cf.save:
        save_krt_routes(key, dev, ip, cf.datadir)
    else:
        check_krt_routes_timeout(key, dev, ip)


def save_krt_routes(key: str, dev: str, ip: int, loc: str = "temp") -> None:
    os.system(
        f"""\
        tests/get_stdout_krt \
        'ip netns exec {dev}' \
        '-{ip}' \
        'table main' > {loc}/{key}{ip}-{dev}
        """
    )


def check_krt_routes_timeout(key: str, dev: str, ip: int) -> None:
    timeout = 60
    for sec in range(timeout):
        if check_krt_routes(key, dev, ip):
            assert 1
        elif sec == timeout - 1:
            assert 0
        else:
            time.sleep(1)


def check_krt_routes(key: str, dev: str, ip: int) -> None:
    save_krt_routes(key, dev, ip)
    current_table = read_file(f"temp/{key}{ip}-{dev}")
    saved_table = read_file(f"{cf.datadir}/{key}{ip}-{dev}")

    for _ in current_table:
        return saved_table == current_table


def test_bird_routes(key: str, dev: str, ip: int = 4) -> None:
    if cf.save:
        save_bird_routes(key, dev, ip, cf.datadir)
    else:
        check_bird_routes_timeout(key, dev, ip)


def save_bird_routes(key: str, dev: str, ip: int, loc: str = "temp") -> None:
    os.system(
        f"""\
        tests/get_stdout_bird \
        '{dev}' \
        'table master{ip}' > {loc}/{key}{ip}-{dev}
        """
    )


def check_bird_routes_timeout(key: str, dev: str, ip: int) -> None:
    timeout = 60
    for sec in range(timeout):
        if check_bird_routes(key, dev, ip):
            assert 1
        elif sec == timeout - 1:
            assert 0
        else:
            time.sleep(1)


def check_bird_routes(key: str, dev: str, ip: int) -> None:
    save_bird_routes(key, dev, ip)
    current_table = read_file(f"temp/{key}{ip}-{dev}")
    saved_table = read_file(f"{cf.datadir}/{key}{ip}-{dev}")

    for _ in current_table:
        return saved_table == current_table


def wait(sec: int):
    time.sleep(sec)


def write_krt_routes(name: str, content: str) -> None:
    with open(name, "w") as txt:
        txt.write(content)


def read_file(name: str) -> None:
    with open(name, "r") as txt:
        return txt.read().split("\n")


def modify_command(dev: str) -> str:
    cmd = f"cd {dev} && sudo ./birdc -l show protocols"
    return cmd


def save_stdout(cmd: str) -> str:
    """Run the command :cmd: and return it as variable (stdout)"""
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    proc_stdout = process.communicate()[0].strip()

    return proc_stdout.decode("utf-8")


def get_attributes_from_output(data: str, protocol: str) -> list:
    """Parse the string from parameter and return list"""
    return [line.split() for line in data.split("\n") if line.startswith(protocol)]


def check_running_protocols(data: list) -> None:
    """Assertion that all protocols are running properly"""
    assert "Running" in data


def check_protocol_state(dev: str, protocol: str) -> None:
    """
    1. Modify the specified bash command with proper variable
    2. Send bash command into the function and return output as str
    3. Collect all desirable lines into single list
    4. If every single line contains "Running" as a state --> pass
    """
    command = modify_command(dev)
    decoded = save_stdout(command)
    clean_str = get_attributes_from_output(decoded, protocol)

    for line in clean_str:
        check_running_protocols(line)
