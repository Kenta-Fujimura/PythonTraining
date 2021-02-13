import random
game = 0
my_card = {0:'市民',0:'市民',0:'市民',0:'市民',1:'奴隷'}
cpu_card = [0,0,0,0,2]
print('ようこそeカードゲームへ')
get_key = input('enter>>')
if get_key == "":
    game = game + 1
    print(f'{game}戦目')
    print(f'手持ちのカード:市民{my_card.count(0)}枚 奴隷{my_card.count(1)}枚')
    my_select = int(input('カード選択:市民なら0 、奴隷なら1 を入力>>'))
    print('カードオープン')
get_key = input('enter>>')
if get_key == "":
    print('あなた: 市民 PC: 市民
