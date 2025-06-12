# # 1. 合図(!!!!)を出力する
# # 2. エンターを入力させる
# # 3. エンターが押されたことを表示する

# print("!!!!!")
# input("エンターキーを押してください:")
# print("エンターキーが押されました。")
# ----

# 1. 待つ秒数をランダムに決める
# 2. その秒数だけ待つ
# 3. 待った後に合図を出す

# 4. 時間の記録を出す (始まった時刻を表示)
# 5. 時間の記録を出す (終わった時刻を表示)
# 6. かかった秒数を出す

import random  # ランダムモジュール（ランダム機能）を使う宣言
import time  # 時間モジュール（時間機能）を使う宣言


# 待つ秒数をランダムに決める
byousuu = random.randint(3, 5)
print(f"待つ秒数: {byousuu}秒")
# 実際に待つ
time.sleep(byousuu)

# 開始時刻を記録
start_time = time.time()
print(f"開始時刻: {start_time}")  # 開始時刻を表示
print("!!!!!")
input("エンターキーを押してください:")


end_time = time.time()  # 終了時刻を記録
print(f"終了時刻: {end_time}")  # 終了時刻を表示
# かかった秒数を出す
kakatta_byousuu = end_time - start_time
print(f"かかった時間: {kakatta_byousuu}秒")
if kakatta_byousuu < 0.01:  # かかった秒数が ０．０１ 未満だったら:
    print("不正をしていますね！")

print("エンターキーが押されました。")
