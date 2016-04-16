import sys
import xml.etree.ElementTree as ET
import bz2
import argparse


def get_page(wiki_file):
  page_lines = []
  page_started, page_ended = False, False

  while not page_started:
    line = str(wiki_file.readline().decode('utf-8'))
    if line == '':
      # readline()が空文字を返したら終了
      return False
    if str(line).find("<page>") != -1:
      page_started = True
      page_lines.append(line)
  
  while not page_ended:
    line = str(wiki_file.readline().decode('utf-8'))
    if line.find("</page>") != -1:
      page_ended = True
    page_lines.append(line)

  return "\n".join(page_lines)



def get_wiki(word):
  input_path = 'jawiki-latest-pages-articles-multistream.xml.bz2'
  #Wikipediaの圧縮ファイルをパースする
  # bz2形式の圧縮ファイルをオープン
  wiki_file = bz2.BZ2File(input_path)
  while True:
    # ページ単位でXML形式の文字列取得
    page_str = get_page(wiki_file)
    if not page_str:
      break

    # XMLをパースする
    root = ET.fromstring(page_str)
    # 例えば記事のタイトルを取得する場合
    # <title>記事のタイトル</title>
    #title = root.find('title').text.encode('utf-8')
    title = root.find('title').text
    print(title)
    if title == word:
      text = root.find('revision').find('text').text
      break
  return text
    #print(title)



#if __name__ == '__main__':
  # コマンドライン引数をパース
  #parser = argparse.ArgumentParser()
  #parser.add_argument('input_path',help=u'Wikipediaの記事の圧縮ファイルのパス (例:jawiki-YYYYMMDD-pages-articles.xml.bz2')

  #args = parser.parse_args()
  # ファイルを読みだして記事ごとにパース
  #text = parse_wiki(args.input_path)
  #text = parse_wiki('jawiki-latest-pages-articles-multistream.xml.bz2')
  #print(text)
