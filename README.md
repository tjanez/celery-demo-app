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

Test if the setup succeded by executing:

```
python test/test.py
```

License
-------

This project is licensed GNU GPLv3 or later.

