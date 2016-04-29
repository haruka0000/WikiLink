#coding:utf-8
import codecs
import re
import sys
import tst  # pytst https://github.com/nlehuen/pytst/downloads
import unicodedata

alias = re.compile(ur"_\(.*?\)")
alldigit = re.compile(ur"^[0-9]+$")

def isValid(word):
    """wordが登録対象の単語のときTrueを返す"""
    # 1文字の単語は登録しない
    if len(word) == 1:
        return False
    # コジコジ_(小惑星)のように別名は登録しない
    if alias.search(word) != None:
        return False
    # 数字だけの単語は登録しない
    if alldigit.search(word) != None:
        return False
    # 仮名2文字の単語は登録しない
    if len(word) == 2 and unicodedata.name(word[0])[0:8] == "HIRAGANA" and unicodedata.name(word[1])[0:8] == "HIRAGANA":
        return False
    # 仮名、漢字、数字、英字以外の文字を含む単語は登録しない
    for c in word:
        if not (unicodedata.name(c)[0:8] == "HIRAGANA" or
                unicodedata.name(c)[0:8] == "KATAKANA" or
                unicodedata.name(c)[0:3] == "CJK" or
                unicodedata.name(c)[0:5] == "DIGIT" or
                unicodedata.name(c)[0:5] == "LATIN"):
            return False
    return True

def createKeywordTree(filename):
    """ファイルに登録されている見出し語からキーワードツリーを作成して返す"""
    try:
        fp = codecs.open(filename, "r", "utf-8")
    except IOError, e:
        print e
        return None

    tree = tst.TST()
    for line in fp:
        word = line.rstrip()
        if isValid(word):
            tree[word] = True  # wordをTSTに登録
    fp.close()
    return tree

def analysis(text, tree):
    """textからWikipedia見出し語を抽出する"""
    keywords = []
    result = tree.scan(text, tst.TupleListAction())
    for t in result:
        if t[2] == True:
            try:
                word = unicode(t[0], "utf-8")
                keywords.append(word)
            except UnicodeDecodeError:
                print e
                continue
    return keywords

if __name__ == "__main__":
    text = u"""人工知能は、コンピュータに人間と同様の知能を実現させようという試み、
        あるいはそのための一連の基礎技術をさす。
        人工知能という名前は1956年にダートマス会議でジョン・マッカーシーにより命名された。
        現在では、機械学習、自然言語処理、パターン認識などの研究分野がある。"""

    tree = createKeywordTree("jawiki-latest-all-titles-in-ns0")
    keywords = analysis(text, tree)
    for w in keywords:
        print w
