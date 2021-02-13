def plus(num):
    total = 0
    for i in range(num+1):
        total = total + i
    return(total)

def plus2(num):
    return sum(range(num + 1))

def plus3(num):
    ls=[i for i in range(num+1)]

def plus4(num):
    if num <=1:
        return num
    else:
        return num + plus(num-1) 


num = int(input('正の整数>'))
ans = plus4(num)
print(ans)

