def int_input(msg):
    return int(input('{}を入力してください>>'.format(msg)))

def calc_payment(amount,peple=2):
    dnum = amount / peple
    pay = dnum // 100 * 100
    if dnum > pay:
        pay = pay + 100
    payorg = amount - pay * (peple -1)
    return [int(pay),int(payorg)]

def show_payment(pay,payorg,peple=2):
    print('***支払額***')
    print(f'1人あたり{pay}円{peple-1}人、幹事は{payorg}円、総額{amount}円です')

amount = int_input('支払総額');peple = int_input('参加人数')
[pay,payorg] = calc_payment(amount,peple)
show_payment(pay,payorg,peple)

