scores1 ={80,40,50}
scores2 ={80,40,50}
print('scores1のidentity:{}'.format(id(scores1)))
print('scores2のidentity:{}'.format(id(scores2)))

if scores1 == scores2:
    print('同じ内容')
else:
    print('違う内容')

if id(scores1) == id(scores2):
    print('同じ存在です')
else:
    print('違う存在')

if scores1 is scores2:
    print('同じ存在です')
else:
    print('違う存在')
    

