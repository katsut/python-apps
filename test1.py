import random

while True:
    answer = random.randint(1, 100)  # 1から100のランダムな数字を生成
    print(answer)

    result = False  # 正解したかどうか 不正解 (フラグ)
    cnt = 0
    for i in range(5):
        cnt = cnt + 1
        input_line = int(input("1から100の数字を入力してください: "))
        if input_line == answer:
            print("正解です！")
            result = True
            break
        else:
            print("不正解です。")
            if input_line < answer:
                if answer - input_line > 10:
                    print("10以上大きいです")
                else:
                    print("もっと大きい数字ですが、だいぶ近いです")
            else:
                if input_line - answer > 10:
                    print("10以上小さいです")
                else:
                    print("もっと小さい数字ですが、だいぶ近いです")

    if result:
        print(f"ゲームに勝ちました！ あなたは{cnt}回目で正解しました。")
    else:
        print(f"ゲームに負けました。正解は{answer}でした。")

    ans = input("もう一度やりますか？(yes/no): ")
    if ans != "yes":
        print("おつかれさまでした！")
        break
