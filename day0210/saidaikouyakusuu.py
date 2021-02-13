def gcd(x,y):
    if x % y == 0:
        return y
    else:
        return gcd(y,x%y)

x = int(input('正の整数1>'))
y = int(input('正の整数2>'))

ans = gcd(x,y)
print(ans)

