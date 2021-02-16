import random

data=[i for i in range(1,10)]
def showData():
	global data
	for i in range(len(data)):
		print(data[i],end='')
		if (i+1) %3 ==0:
			print()
ans=random.randint(1,9)
showData()
count=0
while True:
	count+=1
	index=int(input('好きな場所の数字を選んで入力してください>>'))-1
	if data[index]==ans:
		print('お宝を見つけました!')
		data[index]='O'
		showData()
		break
	elif data[index]=='X':
		print('選択済みの場所です')
	else:
		print('ハズレです。ここより{}数字の場所にあります'.format('大きな' if ans>data[index] else '小さな'))
		data[index]='X'
	showData()
print(f'あなたはお宝を{count}回で発見しました!')
