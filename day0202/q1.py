height = int(input('何段の階段を作る>>'))
for i in range(height-1,-1,-1):
        print(' '*i,'*'*(height-i))

