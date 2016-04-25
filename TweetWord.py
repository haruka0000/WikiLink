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

# Twitterへの接続
  t = Twitter(auth=OAuth(secretjson["access_token"], secretjson["access_token_secret"], secretjson["consumer_key"], secretjson["consumer_secret"]))
  print("## clear access 01 ##")
  # 検索する
  try:
    followers = t.followers.list(screen_name=my_account, count=100)
  except:
    print("ERROR!!")
    exit()
