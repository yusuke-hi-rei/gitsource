print("================ File open test ================")

f = open("sample.txt", "r")
# ファイルを開きファイルオブジェクトを作成する
# テキストを1000文字読み込む
result = f.read(1000)
print(result)
# ファイルを閉じる(必ず忘れないように)
f.close()

