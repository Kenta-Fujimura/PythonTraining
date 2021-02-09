def add_suffix(names):
    for i in range(len(names)):
        names[i]=names[i]+'さん'
    return names

before_names=['松田','浅木','工藤']
"""
copied_name=list()
for n in before_names:
    copied_name.append(n)
"""
copied_name=before_names[:]
after_names=add_suffix(copied_name)

print('さん付け後：'+after_names[0])
print('さん付け前：'+before_names[0])


