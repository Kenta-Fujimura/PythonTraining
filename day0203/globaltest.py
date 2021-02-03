name = '松田'
def change_name():
    global name
    name = '浅木'

def hello():
    print(f'こんにちは{name}さん')

change_name()
hello()

