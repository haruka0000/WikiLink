import Text
import Titles

if __name__ == '__main__':
  target = "5W1H"
  text = Text.get_wiki("言語")
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
      text = Text.get_wiki(w)
      sub_words = set(Text.get_wiki(text))
      all_words = all_words.union(sub_words)
      if target in sub_words:
        print("#### Find!! ####")
        print(target)
        break

    words = all_words

