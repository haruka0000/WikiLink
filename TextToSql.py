import sys
import xml.etree.ElementTree as ET
import bz2
import argparse
import sqlite3

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



def make_sql():
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
    id = root.find('id').text
    body = root.find('revision').find('text').text
    
    print(id + "#####" + title + "#####")
    #print(text)
    
    c.execute('''insert into wiki(id,title,body) values(:id, :title, :body)''', {'id':id, 'title':title, 'body': body})
    conn.commit()


if __name__ == '__main__':
  conn = sqlite3.connect("wikipedia.db")
  c = conn.cursor()
  
  if list(c.execute("select count(*) from sqlite_master where type='table' and name='wiki';"))[0][0] == 0:
    wiki = u"""
      create table wiki(
        id integer primary key,
        title text,
        body text
      );
      """
    c.execute(wiki)
  conn.commit()
  
  make_sql()
