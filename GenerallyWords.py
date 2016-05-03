# -*- coding: utf-8 -*-
#
# Library: 
#   https://github.com/sixohsix/twitter
#
# Twitter Search API
#   https://dev.twitter.com/rest/public/search
#   https://dev.twitter.com/rest/reference/get/search/tweets
#
# Twitter API Limits
#   450 queries per 15 minute for seach api
#   https://dev.twitter.com/rest/public/rate-limiting
# 
import json
from twitter import *
import urllib.request
import Titles

def twt_get(s):
  # OAuth2.0用のキーを取得する
  with open("secret.json") as f:
    secretjson = json.load(f)

  # Twitterへの接続
  t = Twitter(auth=OAuth(secretjson["access_token"], secretjson["access_token_secret"], secretjson["consumer_key"], secretjson["consumer_secret"]))
  print("## clear access 01 ##")
  # 検索する
  try:
    t_words = t.search.tweets(q=s,count=100)
    return t_words
  except:
    return "ERROR!!"
    exit()

def got_words(sample):
  words = []
  for s in sample:
    for t in twt_get(s)['statuses']:
      text = t['text']
      #print(text)
      words = words + Titles.get_titles(text)
    words = sorted(words)
    #print(words)
  return words

def wordsCount(sample):
  count_dict = {}
  words = got_words(sample)

  for ws in list(set(words)):      #0で初期化
    count_dict[ws] = 0

  for w in words:                 #カウント
    count_dict[w] = count_dict[w] + 1

  sorted_dict = {}
  sorted_dict = sorted(count_dict.items(), key=lambda x:x[1], reverse = True)
  #print(sorted_dict)
  return sorted_dict

def general_words(sample):
  words = []
  s_words = wordsCount(sample)
  for sw in s_words:
    if sw[1] >= 20:
      words.append(sw[0])
  return words

if __name__ == '__main__': 
  f = open('General_words.txt', 'w') # 書き込みモードで開く 
  sample = ["今日","最近","RT","私","拡散"]
  for i in range(0,3):
    sample = list(set(sample).union(set(general_words(sample))))
  for s in sample:
    f.write(s + ",") # 引数の文字列をファイルに書き込む
  f.close() # ファイルを閉じる
  print(sample)

#general_words(["今日"])
#twt_words("井上麻里奈")
#twt_words("#ann0")
