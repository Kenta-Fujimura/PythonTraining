scores={'network':60,'database':80,'security':50}
print(scores)
print(scores['database'])
scores['programming']=65
scores['security']=55
print(scores)
del scores['security']
print(scores)
print(sum(scores.values()))
