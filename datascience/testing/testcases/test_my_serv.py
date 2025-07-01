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
    base_dir = Path(__file__).resolve().parent.parent.parent
    cmargs = shlex.split("python3 my_serv.py")
    service_path = os.path.join(base_dir, 'service')
    # change the current working directory to the service path for subprocess
    os.chdir(service_path)
    # raise Exception(os.getcwd())
    result = subprocess.Popen(cmargs)
    pid = result.pid
    # Wait for the service to finish
    time.sleep(2)
    kill_pid(pid)