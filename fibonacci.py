def fib(num):
    assert(num > 0), "Input Must be greater than 0"
    if(num < 0):
        return "Error"
    if(num <= 2):
        return num - 1
    else:
        return fib(num - 1) + fib(num -2)

def fact(num):
    assert(num >= 0), "Input Must not be Negative"
    val = 1
    for x in range(1,num + 1):
        val *= x
    return val

print(fact(0))