Testing multi threading, subprocesses coverage

Command to run:

```
< Clone the repo >
cd coverage_demo
pip install -r requirements.txt
cd datascience
pytest testing/testcases/test_my_serv.py -s -v
```

Command to run coverage:

```
coverage run -m pytest -c testing/config/pytest.ini testing/testcases/test_my_serv.py -s -v
coverage combine                                              
coverage report -m
```