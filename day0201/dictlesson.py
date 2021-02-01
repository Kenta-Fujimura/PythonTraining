dict1=dict()#空のdict
dict1['apple']='りんご'
dict1['orange']='みかん'
print(dict1)

print('要素数',len(dict1))
dict1['banana']='ばなな'

del dict1['orange']
print(dict1)

print(dict1['apple'])#参照

# print(dict1['pine']) #error
print(dict1.get('pine')) #None

if 'apple' in dict1:
    print('appleは含まれている')

if 'pint' not in dict1:
    print('pineは含まれていない')

if 'りんご' in dict1.values():
    print('りんごは含まれている')


