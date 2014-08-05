from __future__ import absolute_import

import random
import signal
import sys
import threading
import time

# Dictionary mapping from signal numbers to their names
signal_names = dict((k, v) for v, k in signal.__dict__.iteritems() 
                    if v.startswith("SIG"))

def signal_handler(signal, frame):
    """Print a message about the received signal and exit."""
    print "{} received {}. Exiting...".format(sys.argv[0],
        signal_names[signal])
    sys.exit(0)

# Handle the ordinary SIGTERM signal.
signal.signal(signal.SIGTERM, signal_handler)
# Handle the SIGINT signal (i.e. Ctrl+C).
signal.signal(signal.SIGINT, signal_handler)

# Import available tasks
from proj.tasks import add, mul, xsum, fib

def run_tasks(tasks, delay=1, queue="default"):
    """Repeatedly choose a Celery task from the given tasks list and execute
    it with the given delay.

    Arguments:
    tasks : list
        List of Celery tasks to choose from.
    delay : int or float (optional)
        Delay between execution of two successive Celery tasks.
    queue : string
        Name of the queue 

    """
    while True:
        t = random.choice(tasks)
        print "Executing task: {}".format(t)
        t.apply_async(queue=queue)
        time.sleep(delay)

# A list of short-running tasks
short_running_tasks = [add.s(2, 2), mul.s(10, 12), xsum.s(range(10))]
# A list of long-running tasks
long_running_tasks = [fib.s(35), fib.s(36), fib.s(37)]

short_t = threading.Thread(target=run_tasks, args=(short_running_tasks,),
                           kwargs={"delay" : 1, "queue" : "hipri"})
long_t = threading.Thread(target=run_tasks, args=(long_running_tasks,),
                          kwargs={"delay" : 5})

for t in [short_t, long_t]:
    # set thread to a daemon thread so that it doesn't block the main program
    # from exiting
    t.daemon = True
    t.start()

# Wait for an interrupt signal.
while True:
    time.sleep(1)

