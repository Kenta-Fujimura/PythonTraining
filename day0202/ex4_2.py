count = 1
ans = True
print('カレーを召し上げれ')
while ans == True:
    print('{}皿のカレーを食べました'.format(count))
    key = input('おかわりはいかがですか？(y/n)>>')
    if key == 'y':
        count += 1
    else:
        ans = False
print('ごちそうさまでした')

