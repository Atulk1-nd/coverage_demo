Testing multi threading, subprocesses coverage

Command to run:

```
cd datascience
pytest testing/testcases/test_my_serv.py -s -v
```

Command to run coverage:

```
coverage run -m pytest testing/testcases/test_my_serv.py -s -v
coverage combine                                              
coverage report -m
```