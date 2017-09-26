import math

def xN(number):
    return (lambda x: pow(x,number))

def sin():
    return lambda x: math.sin(x)

def cos():
    return lambda x: math.cos(x)

def log(base=10):
    return lambda x:math.log(x,base)

def tg():
    return lambda x:math.tan(x)



