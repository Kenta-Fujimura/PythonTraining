class Hero:
    name='松田'
    hp=100
    def sleep(self,hours):
        print(f'{self.name}は{hours}時間寝た!')
        self.hp+=hours

print('スッキリファンタジー')
h=Hero()
h.sleep(3)
print(f'{h.name}の現在のHPは{h.hp}です')

