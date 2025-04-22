# word-histogram.py
# 英文テキストファイルを読み込み，単語の出現頻度をカウントするプログラム

import sys

def main():
    # コマンドライン引数からファイル名を取得
    if len(sys.argv) != 2:
        print("ファイル名を指定してください")
        sys.exit(1)
    filename = sys.argv[1]

    # ファイルを読み込む
    with open(filename, 'r') as file:
        text = file.read()

    # テキストを小文字に変換
    text = text.lower()

    # テキストを単語に分割
    words = text.split()

    # 単語の出現頻度をカウント
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    # 出現頻度を降順でソート
    sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

    # 出力
    for word, count in sorted_word_count:
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()

# このプログラムは以下の処理を行います:
# 1. コマンドライン引数から英文テキストファイルのパスを受け取ります
# 2. 指定されたファイルを読み込みます
# 3. テキストを全て小文字に変換します