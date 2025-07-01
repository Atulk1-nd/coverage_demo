import os
import signal
import subprocess
import shlex
import pytest
from pathlib import Path

def create_devjson(filepath, data):
    print("creating dev.json if not present at "+str(filepath))
    try:
        fp = open(filepath, 'x')
        if fp:
            fp.write(data)
            print("created dev.json")
            fp.close()
    except FileExistsError as err:
        print("dev.json already exists %s", err)

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


class StartService:
    """
    This will start the service as of now
    Service path = Go to the path(dir) where service manage.py is available for that service
    cmd = command to start the srevice
    log file name  = logs will be generated in same directory where the service is available
    """

    def __init__(self, service_path, cmd, log_file_name, devjson_data) -> None:
        try:
            base_dir = Path(__file__).resolve().parent.parent
            filepath = base_dir.joinpath(service_path).joinpath('config').joinpath('dev.json')
            create_devjson(filepath, devjson_data)
            cmargs = shlex.split(cmd)
            print(cmargs)
            print(service_path)
            os.chdir(service_path)
            output_file = open(log_file_name, 'w+')
            print(output_file)
            print(os.getcwd())
            self.result = subprocess.Popen(cmargs, stdout=output_file, stderr=output_file)
            self.pid = self.result.pid
            st = "pid is {pid}".format(pid=self.pid)
            print(st)
            print(os.getcwd())
        except Exception as e:
            pytest.fail("Failed to Start Service :%s" % str(e))

class StopService:
    def __init__(self, pid):
        kill_pid(pid)
