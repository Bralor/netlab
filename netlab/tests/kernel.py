import os
import time
import subprocess

import tests.config as cf


def wait(sec: int):
    time.sleep(sec)


def write_krt_routes(name: str, content: str) -> None:
    with open(name, "w") as txt:
        txt.write(content)


def read_file(name: str) -> list:
    with open(name, "r") as txt:
        return txt.read().split("\n")


def test_krt_routes(key: str, dev: str, family: str,
                    table: str = "main") -> None:
    if cf.save:
        save_krt_routes(key, dev, family, table)
    else:
        check_krt_routes_timeout(key, dev, family, table)


def save_krt_routes(key: str, dev: str, family: str,
                    table: str, loc: str = cf.datadir) -> None:
    os.system(f""" \
        ip netns exec {dev} \
        ./tests/get_stdout_krt '{family}' 'table {table}' \
        > {loc}/{key}-{dev} \
        """)


def check_krt_routes_timeout(key: str, dev: str,
                             family: str, table: str) -> None:
    timeout = 60
    for _ in range(timeout):
        if check_krt_routes(key, dev, family, table):
            return
        else:
            time.sleep(1)
    assert 0


def check_krt_routes(key: str, dev: str, family: str, table: str) -> bool:
    save_krt_routes(key, dev, family, table, cf.tempdir)
    current_table = read_file(f"{cf.tempdir}/{key}-{dev}")
    saved_table = read_file(f"{cf.datadir}/{key}-{dev}")
    return saved_table == current_table


def test_bird_routes(key: str, dev: str, table: str, opts: str = "") -> None:
    if cf.save:
        save_bird_routes(key, dev, table, opts)
    else:
        check_bird_routes_timeout(key, dev, table, opts)


def save_bird_routes(key: str, dev: str, table: str,
                     opts: str, loc: str = cf.datadir) -> None:
    os.system(f""" \
        ./tests/get_stdout_bird '{dev}' 'table {table}' '{opts}' \
        > {loc}/{key}-{dev} \
        """)


def check_bird_routes_timeout(key: str, dev: str,
                              table: str, opts: str) -> None:
    timeout = 60
    for _ in range(timeout):
        if check_bird_routes(key, dev, table, opts):
            return
        else:
            time.sleep(1)
    assert 0


def check_bird_routes(key: str, dev: str, table: str, opts: str) -> bool:
    save_bird_routes(key, dev, table, opts, cf.tempdir)
    current_table = read_file(f"{cf.tempdir}/{key}-{dev}")
    saved_table = read_file(f"{cf.datadir}/{key}-{dev}")
    return saved_table == current_table


def test_ospf_neighbors(**kwargs) -> None:
    if cf.save:
        save_available_neighbors(
            kwargs["key"],
            kwargs["dev"],
            kwargs["protocol"]
        )
    else:
        check_ospf_neighbors_timeout(
            kwargs["key"],
            kwargs["dev"],
            kwargs["protocol"]
        )


def save_available_neighbors(key: str, dev: str, protocol: str,
                             loc: str = cf.datadir) -> None:
    os.system(f"""./tests/get_ospf_neighbors '{dev}' '{protocol}' \
                  > {loc}/{key}-{protocol}-{dev} """)


def check_ospf_neighbors_timeout(key: str, dev: str,
                                 protocol: str, **kwargs) -> None:
    for _ in range(kwargs.get("timeout", 60)):
        if check_ospf_neighbors(key, dev, protocol):
            return
        else:
            time.sleep(1)

    raise Exception("FAILURE! Neighbors in save/check mode are different!")


def check_ospf_neighbors(key: str, dev: str, protocol: str) -> bool:
    save_available_neighbors(key, dev, protocol, loc=cf.tempdir)

    return read_file(f"{cf.datadir}/{key}-{protocol}-{dev}") \
        == read_file(f"{cf.tempdir}/{key}-{protocol}-{dev}")


def process_command(command: str) -> list:
    """
    Run parameter 'command' inside the Shell and capture the stdout.

    Parameters
    ----------
    command : str
        Specific command for Bird

    Returns
    -------
    stdout : list
        List of splitted lines from stdout

    """
    stdout = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True
    ).communicate()[0]
    return stdout.decode("utf-8").split("\n")


def run_configure(dev: str, conf_file: str) -> None:
    """
    Create command './birdc -l configure', then process and verify the
    variable 'captured_stdout'.

    Parameters
    ----------
    dev : str
        Name of the device
    conf_file : str
        Name of the config file

    Returns
    -------
    None

    """
    command = f"cd {dev} && ./birdc -l configure \'\"{conf_file}\"\'"
    captured_stdout = process_command(command)
    assert (conf_file in captured_stdout[1]
            and "Reconfigured" in captured_stdout[2])


def run_command(dev: str, **kwargs) -> list:
    """
    Create command './birdc -l {args}', then process and return the
    variable 'captured_stdout'.

    Parameters
    ----------
    dev : str
        Name of the device
    args : str
        Different arguments of specific command

    Returns
    -------
    captured_stdout : List
        List of splitted lines from stdout

    """
    command = f"cd {dev} && ./birdc -l {kwargs['command']}"
    return process_command(command)

