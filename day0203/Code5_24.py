def eat(breakfast,lunch='ラーメン',dinner='カレー',deserts=()):
    print(f'朝は{breakfast}を食べました')
    print(f'昼は{lunch}を食べました')
    print(f'夜は{dinner}を食べました')
    for d in deserts:
        print(f'おやつに{d}をたべました')

eat(breakfast='納豆ご飯',dinner='カレーうどん')
eat(dinner='カレーうどん',breakfast='納豆ご飯')
eat('納豆ご飯',dinner='カレーうどん')

eat('トースト','パスタ','カレー',('アイス','チョコ','パフェ'))
