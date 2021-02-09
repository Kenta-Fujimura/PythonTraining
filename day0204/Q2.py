import random
num = int(input('サイコロを何回振る？>>'))
arr = []
for i in range(num):
    r1=random.randrange(1,7)
    arr.append(r1)
print(arr)
result = set(arr)
print(f'合計は{sum(arr)}でした')
print(f'出た目は{result}の{len(result)}種類')

