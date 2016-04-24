import Text
import Titles

if __name__ == '__main__':
  start = "インフィニットストラトス"
  target = "井上麻里奈"
  text = Text.get_wiki(start)[2]
  words = Titles.get_titles(text)
  print(words)

  i = 0
  j = 0
  all_words = set([])

  while(True):
    if target in words:
      print("#### Find!! ####")
      print(target)
      break
      
    for w in words:
      text = Text.get_wiki(w)[2]
      sub_words = set(Titles.get_titles(text))
      all_words = all_words.union(sub_words)
      if target in sub_words:
        print("#### Find!! ####")
        print(target)
        break

    words = all_words

