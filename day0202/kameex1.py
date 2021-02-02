from turtle import *

def hilbert(n, length):
    lhlb(n, length)

def lhlb(n, length):
    if n <= 0:
        return
    rt(90)
    rhlb(n-1, length)
    fd(length)
    lt(90)
    lhlb(n-1, length)
    fd(length)
    lhlb(n-1, length)
    lt(90)
    fd(length)
    rhlb(n-1, length)
    rt(90)

def rhlb(n, length):
    if n <= 0:
        return
    lt(90)
    lhlb(n-1, length)
    fd(length)
    rt(90)
    rhlb(n-1, length)
    fd(length)
    rhlb(n-1, length)
    rt(90)
    fd(length)
    lhlb(n-1, length)
    lt(90)

if __name__ == '__main__':
    pu()
    setpos(-200, 200)
    pd()
    speed(0)
    pensize(4)
    hilbert(6, 6)
    done()
