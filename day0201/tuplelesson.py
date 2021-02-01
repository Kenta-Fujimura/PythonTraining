tuple1=(3,5,7)
print(tuple1)
print(len(tuple1))
print(tuple1[1])
print(sum(tuple1))
list1=list(tuple1)
print(list1)
list1.append(10)
print(list1)

a,b,c=tuple1
print(a,b,c)

x=10
y=20

x,y=y,x
print(x)#20


