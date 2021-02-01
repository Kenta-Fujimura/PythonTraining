list1=[] #空のリスト
list2=list() #空のリスト

list1.append(3)
print(list1)
list1.append(5)
print(list1[0])

list2.append(10)
list2.append(20)
print(list2)

list3=list1+list2
print(list3)

list4=list3*3
print(list4)

print('要素数',len(list4))
print('合計',sum(list4))

del list4[0]#削除
print(list4)

list4.remove(5)#最初に見つけた５を削除
print(list4)

list5=list4[3:8]#3以上8未満
print(list5)

print('最後の要素',list5[-1]) 

