import random
num = int(input('100~1000の範囲の偶数をいくつ生成する>>'))
arr = []
for i in range(num):
    r1=random.randrange(100,1000,2)
    arr.append(r1)
arr2=sorted(arr,reverse=True) 
print(f'{num}個生成しました!降順に表示します{arr2}')


