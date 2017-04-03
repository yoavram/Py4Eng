import matplotlib.pyplot as plt
import numpy as np

import sklearn.datasets
from sklearn.model_selection import train_test_split
from sklearn import linear_model

dataset = sklearn.datasets.fetch_california_housing()
X = dataset['data']
y = dataset['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

alphas = np.logspace(-4, -1, 10)
scores = np.empty_like(alphas)
for i,a in enumerate(alphas):
    lasso = linear_model.Lasso()
    lasso.set_params(alpha=a)
    lasso.fit(X_train, y_train)
    scores[i] = lasso.score(X_test, y_test)
    print('α =', a)
    print('coefs:', lasso.coef_)
    
lassocv = linear_model.LassoCV(alphas=alphas)
lassocv.fit(X_train, y_train)
lassocv_score = lassocv.score(X_test, y_test)
lassocv_alpha = lassocv.alpha_
print('CV, α=', lassocv_alpha)
print(lassocv.coef_)

plt.plot(alphas, scores, '-ko')
plt.axhline(lassocv_score, color='b', ls='--')
plt.axvline(lassocv_alpha, color='b', ls='--')
plt.xlabel(r'$\alpha$')
plt.ylabel('Score')
plt.xscale('log')
sns.despine(offset=15)