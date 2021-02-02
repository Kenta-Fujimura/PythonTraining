def input_scores(name):
    print(f'{name}さんの試験結果を入力してください')
    network = int(input('network>>'))
    database = int(input('database>>'))
    security = int(input('security>>'))
    scores = [network,database,security]
    return scores

def calc_average(scores):
    avg = sum(scores) / len(scores)
    return avg

def output_result(name,avg):
    print(f'{name}さんの平均点は{avg}です')

asagi_scores = input_scores('浅木')
matsuda_scores = input_scores('松田')

asagi_avg = calc_average(asagi_scores)
matsuda_avg = calc_average(matsuda_scores)

output_result('浅木',asagi_avg)
output_result('松田',matsuda_avg)
