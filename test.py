import get_text
if __name__ == '__main__':
    # ファイルを読みだして記事ごとにパース
    text = get_text.get_wiki("ジオン公国")
    print(text)
