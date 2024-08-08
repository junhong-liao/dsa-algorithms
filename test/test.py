import math

def fib2N(x: int) -> int:
    if x in {0, 1}: return x
    return fib2N(x - 1) + fib2N(x - 2)

def fibN(x: int) -> int:
    res = [0, 1]
    if x == 0 or x == 1: return res[x]
    for i in range(2, x + 1):
        res.append(res[i - 1] + res[i - 2])
    return res[x]

def fibC(x: int) -> int:
    gr = ((1 + math.sqrt(5)) / 2)
    grc = ((1 - math.sqrt(5)) / 2)
    return round((gr ** x - grc ** x) / math.sqrt(5))

n = 10
x = fib2N(n)
y = fibN(n)
z = fibC(n)
print(x)
print(y)
print(z)