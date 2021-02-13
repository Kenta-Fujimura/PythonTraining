from random import randint
print('数当てゲームを始めます。三桁の数字を当ててください！')
answer = list()
for n in range(3):
    answer.append(randint(0,9))

is_continue = True
while is_continue == True:
    prediction = list()
    for n in range(3):
        data = int(input('{}桁目の予想入力(0-9)>>'.format(n+1)))
        prediction.append(data)
    hit = 0
    blow = 0
    for n in range(3):
        if prediction[n] == answer[n]:
            hit += 1
        else:
            for m in range(3):
                if prediction[n] == answer[m] and n != m:
                    blow += 1

    print('{}ヒット！{}ボール！'.format(hit,blow))
    if hit == 3:
        print('正解です!')
        is_continue = False
    else:
        if int(input('続けますか？1:続ける 2:終了 >>')) == 2:
            print('正解は{}{}{}でした'.format(answer[0],answer[1],answer[2]))
            is_continue = False
        

