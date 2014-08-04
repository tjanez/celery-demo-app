from __future__ import absolute_import

# Start a Celery worker by executing:
# celery -A proj worker -l info

# Import available tasks
from proj.tasks import add, mul, xsum, fib

# Test short-running tasks
add.delay(2, 2)
mul.delay(10, 12)
xsum.delay(range(100))
fib.delay(10)

# Test medium-running tasks
fib.delay(35)
fib.delay(35)
fib.delay(35)

