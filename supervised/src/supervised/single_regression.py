# rye run python src/supervised/sinple_regression.py

import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from mglearn.datasets import load_extended_boston

def main():
    X, y = load_extended_boston()
    # 75%が訓練データ、25%がテストデータ
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

    plt.style.use('dark_background')
    # 中きょの平均部屋数の列のみ抜き出して、2次元配列に変換
    X_train_single = X_train[:, 5].reshape(-1, 1)
    X_test_single = X_test[:, 5].reshape(-1, 1)

    lm_single = linear_model.LinearRegression()
    lm_single.fit(X_train_single, y_train)

    y_pred_train = lm_single.predict(X_train_single)

    plt.xlabel('RM') # 住居の平均部屋数
    plt.ylabel('MEDV') # 住宅価格
    plt.scatter(X_train_single, y_train)
    plt.plot(X_train_single, y_pred_train, color='red', linewidth=2)
    plt.savefig("outputs/sinple_regression.png")
    # バイアスパラメータ
    print(f'intercept: {lm_single.intercept_:.2f}')
    # 重みパラメータ
    print(f'coef: {lm_single.coef_[0]:.2f}')

    # 訓練データ
    print(f'Train score: {lm_single.score(X_train_single, y_train):.2f}')
    # テストデータ
    print(f'Test score: {lm_single.score(X_test_single, y_test):.2f}')

    plt.show()


if __name__ == '__main__':
    main()