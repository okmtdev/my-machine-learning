#!/bin/bash

filename=$1

total_real=0
total_user=0
total_sys=0

# 10回の実行ループ
for i in {1..10}
do
    # time コマンドの出力を変数に格納
    output=$( (time rye run python $filename) 2>&1 1>/dev/null )

    # 'real', 'user', 'sys' の時間を抽出
    real_time=$(echo "$output" | grep real | awk '{print $2}')
    user_time=$(echo "$output" | grep user | awk '{print $2}')
    sys_time=$(echo "$output" | grep sys | awk '{print $2}')

    # 秒に変換
    real_sec=$(echo $real_time | awk -F'm' '{print $1 * 60 + $2}' | sed 's/s//')
    user_sec=$(echo $user_time | awk -F'm' '{print $1 * 60 + $2}' | sed 's/s//')
    sys_sec=$(echo $sys_time | awk -F'm' '{print $1 * 60 + $2}' | sed 's/s//')

    # 合計時間に加算
    total_real=$(echo "$total_real + $real_sec" | bc)
    total_user=$(echo "$total_user + $user_sec" | bc)
    total_sys=$(echo "$total_sys + $sys_sec" | bc)
done

# 平均時間を計算
avg_real=$(echo "scale=3; $total_real / 10" | bc)
avg_user=$(echo "scale=3; $total_user / 10" | bc)
avg_sys=$(echo "scale=3; $total_sys / 10" | bc)

# 結果を出力
echo "Average real time: $avg_real s"
echo "Average user time: $avg_user s"
echo "Average sys time: $avg_sys s"
