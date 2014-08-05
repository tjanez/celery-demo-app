celery-demo-app
===============

Author: Tadej Janež <tadej.janez@tadej.hicsalta.si>

A demo applicaiton to test Celery based on the [Next steps tutorial](http://docs.celeryproject.org/en/latest/getting-started/next-steps.html).


Development Installation and Setup
----------------------------------
Prerequisites: [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/)

Clone the `git` repository:

```
git clone https://github.com/tjanez/celery-demo-app.git
```

Create a virtual environment with `virtualenvwrapper`:

```
mkvirtualenv celery-demo-app -a celery-demo-app/
add2virtualenv ./
toggleglobalsitepackages
```


Usage
-----

To activate the celery-demo-app's virtual environment, execute:

```
workon celery-demo-app
```

To start a Celery worker, open a terminal, activate celery-demo-app's virtual
environment and execute:

```
celery -A proj worker -l info
```

To test if the setup if working, open a terminal, activate celery-demo-app's
virtual environment and execute:

```
python test/test.py
```

If everything is working correctly, you should see something similar to the
follwing in the Celery worker terminal:

```
[2014-08-05 09:55:43,361: INFO/MainProcess] Received task: proj.tasks.add[99036e0c-d2aa-4242-8cd6-4365f0b66228]
[2014-08-05 09:55:43,364: INFO/MainProcess] Received task: proj.tasks.mul[6406f671-70ab-4386-93e8-d4dd3ab1d9ef]
[2014-08-05 09:55:43,367: INFO/MainProcess] Received task: proj.tasks.xsum[30bc3851-6f76-48b0-91e5-1b9b4a9a892e]
[2014-08-05 09:55:43,371: INFO/MainProcess] Received task: proj.tasks.fib[22d8b165-fa6c-4429-85c0-0d58f667758b]
[2014-08-05 09:55:43,374: INFO/MainProcess] Received task: proj.tasks.fib[e9c6fe51-a7a7-4cd7-b204-e9641b1a1cbe]
[2014-08-05 09:55:43,377: INFO/MainProcess] Received task: proj.tasks.fib[960d8ec5-b127-4311-94a6-b850fe4e04f5]
[2014-08-05 09:55:43,381: INFO/MainProcess] Received task: proj.tasks.fib[d5b54b67-9e2f-4469-9b77-33efa52d9e62]
[2014-08-05 09:55:43,414: INFO/MainProcess] Task proj.tasks.add[99036e0c-d2aa-4242-8cd6-4365f0b66228] succeeded in 0.0516921629999s: 4
[2014-08-05 09:55:43,450: INFO/MainProcess] Task proj.tasks.mul[6406f671-70ab-4386-93e8-d4dd3ab1d9ef] succeeded in 0.0365550629999s: 120
[2014-08-05 09:55:43,477: INFO/MainProcess] Task proj.tasks.xsum[30bc3851-6f76-48b0-91e5-1b9b4a9a892e] succeeded in 0.025943415s: 4950
[2014-08-05 09:55:43,517: INFO/MainProcess] Task proj.tasks.fib[22d8b165-fa6c-4429-85c0-0d58f667758b] succeeded in 0.040634902s: 55
[2014-08-05 09:55:49,141: INFO/MainProcess] Task proj.tasks.fib[e9c6fe51-a7a7-4cd7-b204-e9641b1a1cbe] succeeded in 5.62863908s: 9227465
[2014-08-05 09:55:54,333: INFO/MainProcess] Task proj.tasks.fib[960d8ec5-b127-4311-94a6-b850fe4e04f5] succeeded in 5.189894746s: 9227465
[2014-08-05 09:55:59,601: INFO/MainProcess] Task proj.tasks.fib[d5b54b67-9e2f-4469-9b77-33efa52d9e62] succeeded in 5.268263242s: 9227465
```


License
-------

This project is licensed GNU GPLv3 or later.

