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

      if len(set(target_words).intersection(set(words))) != 0:
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


