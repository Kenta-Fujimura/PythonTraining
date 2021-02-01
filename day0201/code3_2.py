name =input('あなたの名前を教えてください>>')
print('{}さん、こんにちは'.format(name))
food = input('{}さんの好きな食べ物を教えてください>>'.format(name))
if food=='カレー':
    print('カレー最高')

else:
    print('私も{}が好きですよ'.format(food))


if 'ラーメン' in food:
        print('ラーメンが含まれています')
if 'ラーメン' not in food:
        print('ラーメンが含まれてません')

isError=False
n=50

if isError and n <100:
    pass
num=10
if num % 2 == 0:
    print('even')

aisatsu = 'さようなら'
if aisatsu == 'こんにちは':
    print('ようこそ')
elif aisatsu == '景気は？':
    print('ぼちぼちです')
elif aisatsu == 'さようなら':
    print('お元気で')
else:
    print('どうした？')
    
number=10
div = '偶数' if number % 2 == 0 else '奇数'
print('{}です'.format(div))

result='you' if score>=80 else 'ryou' if score >=60 else 'ka' if score >= 40 else 'fuka'


