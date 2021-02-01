scores={70,80,55,80}
scores.add(80)
print(scores)
print('要素数は{}'.format(len(scores)))
print('合計は{}'.format(sum(scores)))


list1=[2,3,43,2,41,5,2,6,41,5,6]
print(len(set(list1)))#種類

scores={'network':60,'database':80,'security':60}
members=['松田','浅木','工藤']
print(tuple(members))
print(list(scores))
print(set(scores.values()))

dict1=dict(zip(['赤','緑','青'],['r','g','b']))
print(dict1)

matsuda_scores={'network':60,'database':80,'security':50}
asagi_scores={'network':80,'database':75,'security':92}
member_scores={
        '松田':matsuda_scores,
        '浅木':asagi_scores
}
print(member_scores['松田']['network'])
print(len(member_scores))

member_hobbies={
        '松田':{'sns','まあじゃん','自転車'},
        '浅木':{'まあじゃん','食べ歩き','数学','数学','数学'}
}
print(member_hobbies)
print(member_hobbies['松田'])
print(member_hobbies['浅木'])

common_hobbies=member_hobbies['松田'] & member_hobbies['浅木']
print(type(common_hobbies))
print(common_hobbies)

a=[1,2,3]
b=[4,5,6]
c=[a,b]

print(c)
print(c[0])
print(c[1][2])


A={1,2,3,4}
B={2,3,4,5}
print('和集合',A|B)
print('積集合',A&B)
print('差集合',A-B)
print('対象差',A^B)



