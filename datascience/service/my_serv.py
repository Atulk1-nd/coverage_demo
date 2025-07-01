import multiprocessing
import os, sys
from django_func import create_logger

def my_serv():
    # This is a placeholder function for my_serv.py
    with open("/Users/atulkishor/WORK/coverage_demo/my_serv.log", "w") as log_file:
        log_file.write("Service started successfully.\n")
    print("Service started successfully.")
    create_logger(sys.argv)

def main():
    p = multiprocessing.Process(target=my_serv)
    p.start()
    p.join()  # Wait for the process to finish
    print("Service process has finished.")

if __name__ == '__main__':
    main()