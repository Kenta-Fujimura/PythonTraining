hiragana_1 = 'しりとり'
used_hiragana = []
count = 1
print('しりとりスタート！')
print(hiragana_1)
while True:
    print(f'{count}ターン目です。')
    hiragana_2 = str(input(f'[{hiragana_1[-1]}]ではじまるひらがなを入れてください: '))
    if hiragana_2[0] != hiragana_1[-1]:
        print('最初の文字が間違っています。あなたの負けです。')
        break
    elif hiragana_2 in used_hiragana:
        print('この単語は既に使われています。あなたの負けです。')
        break
    elif hiragana_2[-1] == 'ん':
        print('これは[ん]で終わる単語です。あなたの負けです。')
        break
    else:
        used_hiragana.append(hiragana_1)
        used_hiragana.append(hiragana_2)
        hiragana_1 = hiragana_2
        count = count + 1
