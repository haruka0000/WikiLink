import Text
import Titles
import TweetWords
import GenerallyWords as GW

def wordLink():
  #start = "有川浩"
  start = "クリアファイル"
  #target = "マッチ"
  #start = "僕は友達が少ない"
  target = "井上麻里奈"
  #text = Text.get_wiki(start)[2]  ## [id,title,text]
  #words = Titles.get_titles(text)
  #print(words)
  sample = ["今日","RT","拡散","最近","フォロ","ワー","放送","発売","画像"]
  gen_words = GW.general_words(sample)
  print(gen_words)

  routes = []
  result = ["### ERROR ###"]

  routes.append([start])
  

  tgt_words = TweetWords.twt_words(target)
 
  while True:
    next_routes = []

    if result[-1] == target:
      break

    for r in routes:
      tgt_words = list(set(tgt_words) - set(r[-1]))[:]
      words = list(set(TweetWords.twt_words(r[-1])) - set(gen_words))
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

