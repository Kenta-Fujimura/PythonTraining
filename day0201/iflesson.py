import random
x=random.randint(-100,100)
if x>0:
    print(x,' は正の数です',sep='')
else:
    print(x,' は正の数ではありません',sep='')

score=random.randint(0,100)
print(score)
if score > 80:
    print('優')
elif score > 60:
    print('良')
elif score > 40:
    print('可')
else:
    print('不可')
