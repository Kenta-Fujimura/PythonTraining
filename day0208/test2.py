import pystan

import matplotlib.pyplot as plt

import seaborn as sb

import numpy as np

 

ModelScript = """

    data {

        int N0;

        int N1;

        int k0;

        int k1;

    }

    parameters {

        real<lower = 0.0, upper = 1.0> p0;

        real<lower = 0.0, upper = 100.0> f;

    }

    transformed parameters {

        real<lower = 0.0, upper = 1.0> p1;

        p1 = p0 * (1.0 - f / 100.0);

    }

    model {

        k0 ~ binomial(N0, p0);

        k1 ~ binomial(N1, p1);

    }

"""

 

Data = {'N0': 20568, 'N1': 20567,

        'k0': 162,   'k1': 8}

 

sm = pystan.StanModel(model_code = ModelScript)

fit = sm.sampling(data = Data, n_jobs = 1)

print(fit)

 

plt.rcParams['font.family'] = ['Yu Gothic', 'Noto Sans CJK JP', 'Hiragino Maru Gothic Pro']

 

p0 = np.percentile(fit['p0'], 50.0)

p1 = np.percentile(fit['p1'], 50.0)

sb.kdeplot(fit['p0'], label = '偽 薬')

sb.kdeplot(fit['p1'], label = 'ワクチン')

plt.title('ワクチン: {0:.2e}      偽 薬: {1:.2e}'.format(p1, p0), fontsize = 16)

plt.yticks([])

plt.xlabel('確 率', fontsize = 16)

plt.legend(fontsize = 14)

plt.tight_layout()

 

f_2p5, f_50, f_97p5 = np.percentile(fit['f'], [2.5, 50.0, 97.5])

plt.figure()

sb.kdeplot(fit['f'])

plt.title('中央値 = {0:.1f}\n95%CI = [{1:.1f}, {2:.1f}]'.format(f_50, f_2p5, f_97p5),

          fontsize = 16)

plt.yticks([])

plt.xlabel('効 果', fontsize = 14)

plt.tight_layout()

 

plt.show()
