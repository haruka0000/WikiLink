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

def twt_get(target):
  # OAuth2.0用のキーを取得する
  with open("secret.json") as f:
    secretjson = json.load(f)

  # Twitterへの接続
  t = Twitter(auth=OAuth(secretjson["access_token"], secretjson["access_token_secret"], secretjson["consumer_key"], secretjson["consumer_secret"]))
  print("## clear access 01 ##")
  # 検索する
  try:
    t_words = t.search.tweets(q=target,count=100)
    return t_words
  except:
    return "ERROR!!"
    exit()

def got_words(target):
  words = []
  for t in twt_get(target)['statuses']:
    text = t['text']
    #print(text)
    words = words + Titles.get_titles(text)
    words = sorted(words)
  #print(words)
  return words

def wordsCount(target):
  count_dict = {}
  words = got_words(target)

  for ws in list(set(words)):      #0で初期化
    count_dict[ws] = 0

  for w in words:                 #カウント
    count_dict[w] = count_dict[w] + 1

  sorted_dict = {}
  sorted_dict = sorted(count_dict.items(), key=lambda x:x[1], reverse = True)
  print(sorted_dict)
  return sorted_dict

def twt_words(target):
  words = []
  s_words = wordsCount(target)
  for sw in s_words:
    words.append(sw[0])
  return words
print(twt_words("井上麻里奈"))
#twt_words("井上麻里奈")
#twt_words("#ann0")
