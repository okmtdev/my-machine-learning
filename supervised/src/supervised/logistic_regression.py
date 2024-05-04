# rye run python src/supervised/logistic_regression.py

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn import linear_model
from sklearn.model_selection import train_test_split
from mlxtend.plotting import plot_decision_regions

def main():
    plt.style.use('dark_background')
    np.random.seed(0) # 乱数シードを固定

    # 二次元ガウス分布で模擬データ100人分を作成
    mean = [10, 10] # 平均点
    cov = [[10, 3], [3, 10]] # 分散共分散行列
    x1, y1 = np.random.multivariate_normal(mean, cov, 100).T # 二次元データ生成
    true_false = np.random.rand(100) > 0.9 # 0-1の一様乱数の10%がTrue
    label1 = np.where(true_false, 1, 0) # Advanced indexingでLabelデータ生成

    mean = [20, 20]
    cov = [[8, 4], [4, 8]]
    x2, y2 = np.random.multivariate_normal(mean, cov, 100).T
    true_false = np.random.rand(100) > 0.1  # 0-1の一様乱数の90%がTrue
    label2 = np.where(true_false, 1, 0)

    X = (np.r_[x1, x2]) # 配列の結合
    Y = (np.r_[y1, y2])
    label = (np.r_[label1, label2])

    # ロジスティック回帰
    Data = (np.c_[X, Y])
    X_train, X_test, y_train, y_test = train_test_split(Data, label, random_state=0)
    clf = linear_model.LogisticRegression(random_state=0)
    clf.fit(X_train, y_train)
    plot_decision_regions(X_test, y_test, clf=clf, legend=2)

    print(f'Accuracy: {clf.score(X_test, y_test):2f}')

    label_prenew = clf.predict([[20, 15]])
    print(f'新たな顧客のラベルは{label_prenew}です。')


    plt.scatter(X[label == 1], Y[label == 1], marker='^', s=30, c='blue', label='1:continue')
    plt.scatter(X[label == 0], Y[label == 0], marker=',', s=30, c='red', label='0:withdraw')
    plt.xlabel("Annual number of purchases")
    plt.ylabel("Average purchase price")
    plt.legend(loc="lower right")
    plt.savefig("outputs/logistic_regression.png")
    plt.show()


if __name__ == '__main__':
    main()