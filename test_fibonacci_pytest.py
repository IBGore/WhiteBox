import fibonacci as f

#Fibonacci Tests
def test_fib1():
    assert(f.fib(1) == 0)

def test_fib2():
    assert(f.fib(2) == 1)


def test_fib3():
    assert(f.fib(3) == 1)

#Factorial Tests
def test_fact1():
    assert(f.fact(0) == 1)

def test_fact2():
    assert(f.fact(1) == 1)

def test_fact3():
    assert(f.fact(2) == 2)

def test_fact4():
    assert(f.fact(3) == 6)