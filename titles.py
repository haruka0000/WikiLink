import MeCab
import sys

m = MeCab.Tagger("-u wikipedia_title.dic")

text = u"テキストからWikipediaに登録されている見出し語を抽出したいという目的は同じですが、今度は、MeCabを使わずに別のアプローチを試みます。入力した任意のテキストから辞書に登録されている単語を切り出したい場合は、Trieというデータ構造が使えます"

data = m.parse(text).split("\n")
titles = []
for d in data:
  n = d.split(",")
  if n[-1] == "wikipedia":
    titles.append(n)
  #print(n[-1:])

words = []
for t in titles:
  words.append(t[0].split("\t")[0])

print(words)
