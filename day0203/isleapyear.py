def is_leapyear(y):
    return(y%400==0 or (y%4==0 and y % 100 != 0))

current_year = int(input('西暦>>'))
if is_leapyear(current_year):
    print(f'西暦{current_year}年は、うるう年')
else:
    print(f'西暦{current_year}年は、うるう年ではない')



