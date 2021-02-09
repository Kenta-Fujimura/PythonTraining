class Human:
    def __init__(self,name,year,birth):
        self.name=name
        self.year=year
        self.birth=birth
    def introduce(self):
        return f'私の名前は{self.name}。今年で{self.year}'
    def grow_old(self,after):
        self.year+=after

human1=Human('kawada',26,19931013)
print(human1.name)
print(human1.introduce())
human2=Human('Yamada',30,19890703)
print(human2.name)
print(human2.introduce())
human2.grow_old(2)
print(human2.introduce())

class HumanHealth(Human):
    def __init__(self,name,year,birth,height,weight):
        super().__init__(name,year,birth)
        self.height=height
        self.weight=weight

    def get_bmi(self):
        return round(self.weight/(self.height**2),2)

    def introduce(self):
        return super().introduce()+f'BMIは{self.get_bmi()}'
        

human3=HumanHealth('souma',26,19931230,1.75,68)
print(human3.get_bmi())
print(human3.introduce())



