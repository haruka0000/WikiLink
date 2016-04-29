import Text
import Titles
import TweetWord

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
  
  ## startの単語を絞る（start単語に関連する見出し語 && twitterから取れる関連語）
  twtr_start = TweetWord.twt_words(start)
  print("##  START WORDS FROM TWITTER")
  print(twtr_start)

  target_text = Text.get_wiki(target)[2]  ## [id,title,text]
  target_words = list(set(Titles.get_titles(target_text)))
  twtr_words = TweetWord.twt_words(target)
  print("============ GET FROM TWITTER =============")
  print(twtr_words)
  filter_words = []   ## targetに関する単語の数を絞るために使用
  
  if len(set(target_words).intersection(set(twtr_words))) != 0:
    ## 「targetに関する単語」と、「Twitterより取得したtargetに関する単語」の論理積を取り、更に語を絞る
    filter_words = list(set(target_words).intersection(set(twtr_words)))[:]
    print("============ FILTER CHANGE!! ============")
    print(filter_words)
  else:
    ## 論理積が０になった場合は「targetに関する単語」をそのまま使用する
    filter_words = target_words[:]

  
  while True:
    next_routes = []
    if target == str(result[-1]):
      print(result)
      print("終了！！！")
      break

    for r in routes:
      text = Text.get_wiki(r[-1])[2]  ## [id,title,text]
      words = list(set(Titles.get_titles(text)[:]))
      if target == str(result[-1]):
        break
      print("### ")
      print(words)
      
      if len(routes)==1:
        if len(set(words).intersection(set(twtr_start))) != 0:
          words = list(set(words).intersection(set(twtr_start)))[:]
          print("========== START WORDS FILTERED BY TWITTERS WORDS ==========")
          print(words)


      ## filter_wordsで単語を絞り、計算量を減らす
      if len(set(target_words).intersection(set(filter_words))) != 0:
        words = list(set(target_words).intersection(set(words)))[:]
        print("======== CHANGE! ========")
        print(words)

      for w in words:
        new_route = []
        new_route = r[:]
        new_route.append(w)
        next_routes.append(new_route)
        print(new_route)
        if target == str(new_route[-1]):
          result = new_route[:]
          break

    routes = next_routes[:]     


