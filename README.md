Testing multi threading, subprocesses coverage

Command to run:

```
cd datascience
pytest testing/testcases/test_my_serv.py -s -v

pytest --cov=service --cov-report=term -c  testing/testcases/test_my_serv.py -s -v
```