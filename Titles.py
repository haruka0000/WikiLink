import MeCab
import sys

def get_titles(text):
  m = MeCab.Tagger("-u wikipedia_title.dic")

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

  return(words)
