import os
import sys
import pytest


def init(tdir, mod):
    result = os.system(f"./start -c {tdir}")
    if result != 0:
        return False

    init_dirs(tdir, mod)
    return True


def init_dirs(tdir, mod):
    global temp_dir
    temp_dir = "temp"
    data_dir = f"{tdir}/data"

    if mod == "save":
        init_dir(data_dir)
    elif mod == "check":
        init_dir(temp_dir)


def init_dir(dir):
    if os.path.isdir(dir):
        for _ in os.listdir(dir):
            os.remove(f"{dir}/{_}")
    else:
        os.mkdir(dir)


def run(tdir, mod):
    clean_name = tdir.rstrip("/")
    clean_test = tdir.split("/", 1)[1].rstrip("/")
    print(f"Running {tdir} in {mod.upper()} mode")
    return pytest.main(["-x", "-v", f"{clean_name}/test-{clean_test}.py"]) == 0


def cleanup(tdir, mod):
    clean_dirs(mod)
    os.system(f"./stop && sudo ./clean.sh")
    os.remove("common/runtest_args.pckl")


def clean_dirs(mod):
    if mod == "save":
        return

    for _ in os.listdir(temp_dir):
        os.remove(f"{temp_dir}/{_}")

    try:
        os.rmdir(temp_dir)
    except:
        print("Error in removing temp directory")
