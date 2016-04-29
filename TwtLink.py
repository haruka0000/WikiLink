import Text
import Titles
import TweetWord

if __name__ == '__main__':
  #start = "有川浩"
  start = "布団"
  #target = "マッチ"
  #start = "僕は友達が少ない"
  target = "井上麻里奈"
  #text = Text.get_wiki(start)[2]  ## [id,title,text]
  #words = Titles.get_titles(text)
  #print(words)
  
  routes = []
  result = ["### ERROR ###"]

  routes.append([start])
  

  tgt_words = TweetWord.twt_words(target)
 
  while True:
    next_routes = []

    if result[-1] == target:
      break

    for r in routes:
      tgt_words = list(set(tgt_words) - set(r[-1]))[:]
      words = TweetWord.twt_words(r[-1])
      if target in words:
        result = r[:]
        result.append(target)
        print(result)
        print("終了！！")
        break 
      #print(words)
      
      if len(set(words).intersection(set(tgt_words))) != 0:
        print("====== CHANGE ======")
        words = list(set(words).intersection(set(tgt_words)))[:5]
        print(words)
      else:
        words = words[:3]
  
      for w in words:
        new_route = []
        new_route = r[:]
        new_route.append(w)
        next_routes.append(new_route)
        print(new_route)

    routes = next_routes[:]     


