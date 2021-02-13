import time
cache={}
def fibo(n):
    global cache
    if n in cache:
        return cache[n]
    if n==0:
        result= 0
    elif n==1:
        result= 1
    else:
        result= fibo(n-1)+fibo(n-2)
    cache[n]=result
    return result

for i in range(1,11,5):
    start=time.time()
    result=fibo(i)
    end=time.time()
    duration=end-start
    print(i,result,duration)
