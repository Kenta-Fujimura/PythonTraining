def welcome(u):
    print('ようこそ{}さん'.format(u['name']))
    u['age']=u['age']+1
    print('あなたは来年{}歳だから大吉です！'.format(u['age']))

username=input('name>>')
userage=input('age>>')
user = {'name':username,'age':userage}
user_copied=user.copy()
welcome()
