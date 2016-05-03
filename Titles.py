import MeCab
import sys

def get_titles(text):
  m = MeCab.Tagger("-u wikipedia_title.dic")

  data = m.parse(text).split("\n")[0:-2]
  titles = []
  for d in data:
    n = d.split(",")
    if n[-1] == "wikipedia" and n[0].split("\t")[1] == "名詞":
      titles.append(n)
    #print(n[0].split("\t")[1])

  words = []
  for t in titles:
    words.append(t[0].split("\t")[0])

  return(words)

#print(get_titles("一緒に自分の実力に見合わないことをするやつがクラスに多いながらその筆頭は自分である"))
