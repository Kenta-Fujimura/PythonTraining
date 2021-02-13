import random

cards=['市民','奴隷','皇帝']
user_cards=[0,0,0,0,1]
pc_cards=[0,0,0,0,2]
random.shuffle(pc_cards)
count=0
print('ようこそeカードゲームへ')
while True:
	input('>>enter')
	count+=1;
	print(count,'戦目')
	print('手持ちのカード: 市民',user_cards.count(0),'奴隷:',user_cards.count(1))
	user_card=int(input('カード選択:「市民」なら「0」、「奴隷」なら「1」を入力>>'))
	user_cards.remove(user_card)
	print('カードオープン!')
	input('>>enter')
	pc_card=pc_cards.pop()
	print('あなた:',cards[user_card],'PC:',cards[pc_card])
	if user_card==pc_card:
		print('引き分け!')
		continue
	elif user_card==1 and pc_card==2:
		print('あなたの勝ち!')
		print('Congratulation!')
	else:
		print('あなたの負け!')
		print('GAME OVER')
	break
