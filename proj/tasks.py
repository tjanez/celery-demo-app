from __future__ import absolute_import

from proj.celery import app

@app.task
def add(x, y):
    """Return the sum of x and y.
    
    Arguments
    ---------
    x : int or float
        First augend.
    y : int or float
        Second augend.

    """
    return x + y

@app.task
def mul(x, y):
    """Return the product of x and y.
    
    Arguments
    ---------
    x : int or float
        First multiplicand.
    y : int or float
        Second multiplicand.

    """
    return x * y

@app.task
def xsum(numbers):
    """Return the sum of number in the given iterable.

    Arguments
    ---------
    numbers : iterable
        Numbers to sum.

    """
    return sum(numbers)

@app.task
def fib(n):
    """Return the n'th Fibonacci number.

    NOTE: Implementation is a recursive one. This can be used to test
    long-running CPU-bound Celery tasks.
    
    Arguments
    ---------
    n : int
        A positive integer.
    
    """
    if n < 0:
        raise ValueError("Fibonacci numbers are only defined for n >= 0.")
    return _fib(n)

def _fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return _fib(n - 1) + _fib(n - 2)

