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
import time

def twt_get(s):
  try:
    # OAuth2.0用のキーを取得する
    with open("secret.json") as f:
      secretjson = json.load(f)
    
    # Twitterへの接続
    t = Twitter(auth=OAuth(secretjson["access_token"], secretjson["access_token_secret"], secretjson["consumer_key"], secretjson["consumer_secret"]))
    
    limit = t.application.rate_limit_status()
    for k,v in limit['resources']['search'].items():
      print(k + " " + str(v))
    
    if limit['resources']['search']['/search/tweets']['remaining'] == 1:
      print("#### Waiting 15 minutes to recover access limit ####")
      wait_m = 5
      time.sleep(wait_m * 60)
      
    print("## accessing... ##")
    
    # 検索する
    t_words = t.search.tweets(q=s,count=100)
    return t_words
  except:
    return []

def got_words(sample):
  words = []
  for s in sample:
    while True: 
      twt = twt_get(s)
      if len(twt) != 0:
        break
      print("#### Waiting 15 minutes to recover access limit ####")
      wait_m = 5
      time.sleep(wait_m * 60)
    for t in twt['statuses']:
      #print(t)
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
    if sw[1] >= 40:   # 30/100ツイートに含まれる
      words.append(sw[0])
  return words


if __name__ == '__main__':
  count = 0
  while count < 3:
    f = open('General_words.txt', 'r')
    filetext = ""
    for line in f:
      filetext = filetext + line
    f.close()
    
    gen_words = filetext.split(",")[0:-1]
    
    bef_len = len(gen_words)

    if len(gen_words) == 0:
      gen_words = ["今日","RT","私","自動","bot"]
      
    print(gen_words)
    
    gen_words = list(set(gen_words).union(set(general_words(gen_words))))
    
    f = open('General_words.txt', 'w') # 書き込みモードで開く 
    for g in gen_words:
      f.write(g + ",") # 引数の文字列をファイルに書き込む
    f.close() # ファイルを閉じる
    
    aft_len = len(gen_words)

    if bef_len == aft_len:
      count = count + 1
