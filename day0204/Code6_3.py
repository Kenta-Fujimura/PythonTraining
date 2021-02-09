userinfo = input('名前と血液型をカンマで区切って1行で入力>>')
[name,blood] = userinfo.split(',')
blood = blood.upper().strip()
print(f'{name}さんは{blood}型なので大吉です')

print('{:.1f}'.format(2.342))

str='absjabsjabaskjhsjdhkjhjdsfh'
result = str.count('a')
print(f'aは{result}回出てくる')

for i,s in enumerate('hello',1):
    print(f'{i}文字目は{s}です')
   
s1='hello'
s3=s1[::-1]
print(s3)


