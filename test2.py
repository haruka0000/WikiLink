import Text
import Titles

if __name__ == '__main__':
  #start = "有川浩"
  start = "読売新聞"
  #start = "高橋"
  #start = "僕は友達が少ない"
  target = "井上麻里奈"
  #text = Text.get_wiki(start)[2]  ## [id,title,text]
  #words = Titles.get_titles(text)
  #print(words)
  
  routes = []
  result = ["### ERROR ###"]

  routes.append([start])
  
  target_text = Text.get_wiki(target)[2]  ## [id,title,text]
  target_words = list(set(Titles.get_titles(target_text)))

  f_name = target + "(text).txt"
  f = open(f_name, 'w') # 書き込みモードで開く
  f.write(target_text) # 引数の文字列をファイルに書き込む
  f.close() # ファイルを閉じる

  f_name = target + "(words).txt"
  f = open(f_name, 'w') # 書き込みモードで開く
  f.write("\n".join(target_words)) # 引数の文字列をファイルに書き込む
  f.close() # ファイルを閉じる

  print(target_text)
  print("================================================================\n")
  print(target_words)
