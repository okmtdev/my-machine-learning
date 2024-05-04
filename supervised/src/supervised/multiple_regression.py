# rye run python src/supervised/multiple_regression.py

import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from mglearn.datasets import load_extended_boston

def main():
    X, y = load_extended_boston()
    # 75%が訓練データ、25%がテストデータ
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

    lm= linear_model.LinearRegression()
    lm.fit(X_train, y_train)

    # バイアスパラメータ
    print(f'intercept: {lm.intercept_:.2f}')
    # 重みパラメータ
    print(f'coef: {lm.coef_[:4]}')

    # 訓練データ
    print(f'Train score: {lm.score(X_train, y_train):.2f}')
    # テストデータ
    print(f'Test score: {lm.score(X_test, y_test):.2f}')

    plt.show()


if __name__ == '__main__':
    main()