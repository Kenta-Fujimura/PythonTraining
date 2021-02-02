from turtle import *

def square(length):
    for _ in range(4):
        fd(length)
        rt(90)

def spiral(n, length, angle):
    for _ in range(n):
        square(length)
        rt(angle)
        length = length*1.05


if __name__ == '__main__':
    n = 100
    length = 3
    angle = 10
    speed(0)

    spiral(n, length, angle)
    done()
