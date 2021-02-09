import random
arr = []
a_count = 0
b_count = 0
for i in range(1,100):
    arr.append(i)
random.shuffle(arr)
for j in range(5):
    print(f'{j+1}回戦')
    a_score = arr.pop(0)
    b_score = arr.pop(0)
    if a_score > b_score:
        result = 'Aの勝ち'
        a_count = a_count + 1
    else:
        result = 'Bの勝ち'
        b_count = b_count + 1
    print(f'A:{a_score},B:{b_score}…{result}')
if a_count > b_count:
    result2 = 'Aの勝ち'
else:
    result2 = 'Bの勝ち'
print(f'{a_count}対{b_count}で{result2}')

    

