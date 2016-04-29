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

def twt_words(target):
  words = set([])
  for t in twt_get(target)['statuses']:
    text = t['text']
    #print(text)
    words = words.union(set(Titles.get_titles(text)))
  #print(words)
  return list(words)

#twt_words("井上麻里奈")
#twt_words("#ann0")
