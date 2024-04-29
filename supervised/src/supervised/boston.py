from sklearn.model_selection import train_test_split
from mglearn.datasets import load_extended_boston

def main():
    print('Hello, World!')
    X, y = load_extended_boston()
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)


if __name__ == '__main__':
    main()