import random
arr=[]
for i in range(100):
    ans=random.randint(1,100)
    arr.append(ans)
print(arr)
#print('77->',arr.index(77))

for count in range(100):
    if arr[count]==77:
        print('77->',i)
        break
else:
    print('なし')

