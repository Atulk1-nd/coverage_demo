import os
import signal
import subprocess
import shlex
from pathlib import Path
import time

def kill_pid(pid):
    """
     Kills the pid
    :param pid: process id
    :return: True
    """
    try:
        os.kill(int(pid), signal.SIGKILL)
        print("PID {} killed successfully".format(pid))
    except OSError:
        print("No processes was running or Permission denied or Process killed internally")
    return True

def test_my_serv():
    env = os.environ.copy()
    cmargs = shlex.split("python3 -m service.my_serv 90")
    result = subprocess.Popen(cmargs, env=env)
    pid = result.pid
    # Wait for the service to finish
    time.sleep(2)
    kill_pid(pid)