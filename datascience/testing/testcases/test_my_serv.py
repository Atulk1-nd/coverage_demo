import os
import signal
import subprocess
import shlex
from pathlib import Path

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
    os.chdir(service_path)
    # raise Exception(os.getcwd())
    result = subprocess.Popen(cmargs)
    pid = result.pid
    kill_pid(pid)