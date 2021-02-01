n=1 # 最初の個数
minute=0 # 経過時間
days=1 # 検証日数
day_minute=days*60*24 # 分に換算
while minute < day_minute:
    n*=2 # n=n*2と同意、個数を２倍にする
    minute+=5 # n=n+5と同意、５分進める
    print(minute,'分後',n) # 途中経過出力
print(n) # 結果出力

