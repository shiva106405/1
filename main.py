import random

x = 1
print(x)


def fun1():
    global x
    x = 223
    print(x)


fun1()
t = type(x)
print(t)
print(random.randint(1, 5))
