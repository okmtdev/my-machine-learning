# my-machine-learning

- 教師あり学習
  - 分類
  - 推薦
  - 回帰
- 教師なし学習
  - クラスタリング
  - 異常検知
  - 次元圧縮
- 強化学習
  - 機器の制御
  - 戦略の構築
- 生成（合成）
  - 生成と変換

エキスパートシステムと機械学習システム

- エキスパートシステム: 人がルールを決めてシステムを構築する
- 機械学習システム: どんな出力が得られるのか不明である

scikit-learn: 機械学習アルゴリズムを実装するために使用するパッケージ。教師あり学習の分類と回帰、教師なし学習のクラスタリングと異常検知、次元圧縮が得意。

日本語自然言語処理は MeCab、JUMAN、CaboCha、gensim が得意

Choosing the right estimator

![alt text](https://scikit-learn.org/stable/_static/ml_map.png)
https://scikit-learn.org/stable/tutorial/machine_learning_map/index.html

特徴量の正規化: 各特徴量のスケール（値の幅）を調整する操作のこと

特徴量エンジニアリング

データセットの準備段階で重要なのは、データセット全体を訓練データとテストデータに分割すること
