count=0
student_num=int(input('学生の数を入力>>'))
score_list=list()
while count < student_num:
    count+=1
    score=int(input('{}人目の試験の点数を入力>>'.format(count)))
    score_list.append(score)
print(score_list)
total=sum(score_list)
print('平均点は{}点です'.format(total/student_num))
count2=0
while count2 < len(score_list):
    if score_list[count]>=60:
        print('ok')
    else:
        print('ng')
    count += 1
